from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

@app.get("/")
def read_root():
    return {"message":"Hello, FastAPI!"}

@app.get("/item/{item_id}")
def read_item(item_id:int,q:str=None):
    return {"item_id":item_id,"q":q}

class Item(BaseModel):
    name:str
    context:str = None
    price:float

@app.post("/items/")
def create_time(item:Item):
    return {"item":item}


if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=9000)
