from fastapi import FastAPI,status
from pydantic   import BaseModel
from database import SessionLocal
import models

app = FastAPI()
db = SessionLocal()

#to avoid serealized response error
class OurBaseModel(BaseModel):
    class Config:
        orm_mode=True

class Person(OurBaseModel):
    firstName: str
    lastName: str
    isMale: bool
    

@app.get('/',response_model=list[Person],status_code=status.HTTP_200_OK)
def getAll_person():
    getAllPerson = db.query(models.Person).all()
    return getAllPerson


@app.post('/addperson',response_model=Person,status_code=status.HTTP_201_CREATED)
def add_person(person:Person):
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

