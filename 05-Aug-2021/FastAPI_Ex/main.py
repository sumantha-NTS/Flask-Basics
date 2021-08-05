from enum import Enum
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class items(BaseModel):
    name: str
    description: Optional[str]=None
    price: float
    tax: Optional[float] = None
    status: Optional[bool] = 0

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

### path
@app.get('/')
def index():
    return {"message": "Hello, welcome to family"}

@app.get('/user/{name}')
def user(name, q:Optional[str]=None):
    ret = {'Greeting': "Hello, welcome %s" %name}
    if q:
        ret.update({"optinal_entry":q})
    return ret

@app.get("/models/{model_name}")
def get_model(model_name:ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message":"Deep Learning"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    else :
        return {"message": "nothing"}

### request body
@app.post('/items/{item_id}')
def sell_items(item_id:int, item:items):
    result = {"item id": item_id, **item.dict()}
    if item.tax:
        price_wo_tax = item.price - item.tax
        result.update({"Price without tax":price_wo_tax})
    return result