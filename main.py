from fastapi import FastAPI,status , Depends,HTTPException,Body
from pydantic   import BaseModel
from database import get_db
import models
from sqlalchemy.orm import Session
from jose import jwt
from datetime import datetime,timezone,timedelta
from fastapi.security import OAuth2PasswordBearer
from router.login import routerExample

app = FastAPI()

app.include_router(routerExample)
#to avoid serealized response error
class OurBaseModel(BaseModel):
    class Config:
        #orm_mode=True
        from_attributes = True  # Replace `orm_mode` with `from_attributes`

class Person(OurBaseModel):
    firstName: str
    lastName: str
    isMale: bool
    password:str
    
class PersonLogin(OurBaseModel):
    firstName:str
    password:str
    
class PersonResponse(OurBaseModel):
    firstName: str
    lastName: str
    isMale: bool
    password:str|None
    
    
SECRET_KEY="DFJKJ3J2039UR309JFIMFNOEIJF0293UR09U2134U09FJIF0932URJ2309"
ALGORITHM='HS256'

@app.get('/',response_model=list[PersonResponse],status_code=status.HTTP_200_OK)
async def getAll_person(db: Session = Depends(get_db)):
    getAllPerson = db.query(models.Person).all()
    return getAllPerson


@app.post('/addperson',response_model=PersonResponse,status_code=status.HTTP_201_CREATED)
async def add_person(person:Person,db: Session = Depends(get_db)):
    newPerson = models.Person(
        firstName = person.firstName,
        lastName = person.lastName,
        isMale = person.isMale,
        password = person.password
        )
    db.add(newPerson)
    db.commit()
    return newPerson

def passwordAuthentication(username:str,password:str,db:Session=Depends(get_db)):
    getPerson = db.query(models.Person).filter(models.Person.firstName == username).first()
  
    if getPerson.password != password:
        raise HTTPException(status_code=401, detail="Incorrect password")
    
    return True
        
def create_jwt(firstName:str,gender:bool):
    #after 1 hour
    expirationTime = datetime.now(timezone.utc)+timedelta(hours=1)
    #jwt payload
    encode= {'sub':firstName,'gender':gender,"exp":expirationTime}
    
    token = jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

class loginResponse(OurBaseModel):
     data: PersonResponse
     token: str
     

@app.post('/login',response_model=loginResponse,status_code=status.HTTP_200_OK)
async def login(person:PersonLogin=Body(),db:Session=Depends(get_db)):
    getPerson = db.query(models.Person).filter(models.Person.firstName == person.firstName).first()
    
    if not getPerson:
        raise HTTPException(status_code=400,detail="Person not found")
    
    if not passwordAuthentication(getPerson.firstName,person.password,db):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    jwtToken = create_jwt(getPerson.firstName,getPerson.isMale)
    
     # Return user data with the token
    return {
        "data":getPerson,
        "token":jwtToken
    }
    
# OAuth2PasswordBearer provides a Bearer token from the `Authorization` header
getTokenFromHeader = OAuth2PasswordBearer(tokenUrl="token")

def verify_jwt(token: str = Depends(getTokenFromHeader)):
     try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # Returns the decoded payload if valid
     except :
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    

#get paritcular person by jwt
@app.get('/getperson',status_code=status.HTTP_200_OK)
async def get_person(data=Depends(verify_jwt),db:Session=Depends(get_db)):
    personDAta= db.query(models.Person).filter(models.Person.firstName==data['sub']).first()
    
    if not personDAta:
        raise HTTPException(status_code=401,detail="you are not valid user")
    
    return data
     
    

# @app.get('/',status_code=200)
# def getCar_info():
#     return{"message":"server is running"}

# #f string is used to embed the expression inside the string literals using {}
# @app.get('/getpersonByName/{personName}',status_code=200)
# def getPerson_By_Id(personName:str):
#     return{"message":f"your person name is {personName}"}


# @app.post('/addPersonInfo',status_code=200)
# def addPerson_info(person:Person):
#     return (person)
