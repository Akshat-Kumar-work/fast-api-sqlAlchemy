from fastapi import FastAPI
from pydantic   import BaseModel

app = FastAPI()

class Person(BaseModel):
    firstName: str
    lastName: str
    isMale: bool

@app.get('/',status_code=200)
def getCar_info():
    return{"message":"server is running"}

#f string is used to embed the expression inside the string literals using {}
@app.get('/getpersonByName/{personName}',status_code=200)
def getPerson_By_Id(personName:str):
    return{"message":f"your person name is {personName}"}


@app.post('/addPersonInfo',status_code=200)
def addPerson_info(person:Person):
    return (person)

