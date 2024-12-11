from fastapi import FastAPI


app = FastAPI()

@app.get('/',status_code=200)
def getCar_info():
    return{"message":"server is running"}