from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
dict1 = {'name':'Anil', 'age':39,'gender':'male'}

class Item(BaseModel):
    key:str
    value:str
    
@app.get("/")
def get_data():
    return dict1
    
@app.post("/creat_data")
def create_data(item:Item):
    dict1[item.key] = item.value
    return dict1
    
@app.put("/update_data")
def update_data(item:Item):
    if item.key not in dict1:
        raise HTTPException(status_code=404,details="item not found")
    dict1[item.key] = item.value
    return dict1
    
@app.delete("/delete_item")
def delete_item(key:str):
    if key in dict1:
        del dict1[key]
    return dict1
