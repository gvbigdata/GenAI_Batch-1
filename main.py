from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def example(a:int):
    return {'square is ':a**2}
    
#python -m uvicorn main:app --reload
#uvicorn main:app --reload