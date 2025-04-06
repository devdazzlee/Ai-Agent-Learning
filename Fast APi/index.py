from fastapi import FastAPI;
from pydantic import BaseModel

app = FastAPI()

list_Value = [] 

class Product_request(BaseModel):
    _id  : str
    name : str
    description : str
    

@app.get("/")
async def hello():
    return{"message" : "Hello World"} 

@app.get('/ahmed')
def ahmed():
    return{"name" :"ahmed"} 


@app.get('/product/{productId}')
async def product_detail(productId : str):
    return {"Product Detail" : {productId}}

@app.post('/addpost')
async def add_post(post: Product_request):
    await list_Value.insert(post)
    return list_Value