from fastapi import FastAPI,status , Depends
from pydantic   import BaseModel
from database import get_db
import models
from sqlalchemy.orm import Session

app = FastAPI()


#to avoid serealized response error
class OurBaseModel(BaseModel):
    class Config:
        orm_mode=True

class Person(OurBaseModel):
    firstName: str
    lastName: str
    isMale: bool
    

@app.get('/',response_model=list[Person],status_code=status.HTTP_200_OK)
async def getAll_person(db: Session = Depends(get_db)):
    getAllPerson = db.query(models.Person).all()
    return getAllPerson


@app.post('/addperson',response_model=Person,status_code=status.HTTP_201_CREATED)
def add_person(person:Person,db: Session = Depends(get_db)):
    newPerson = models.Person(
        firstName = person.firstName,
        lastName = person.lastName,
        isMale = person.isMale
        )
    db.add(newPerson)
    db.commit()
    return newPerson


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

