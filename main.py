from fastapi import FastAPI, Body, HTTPException, Response, status
from pydantic import BaseModel
from db import PostDatbase
from typing import Annotated



app = FastAPI()

class Post(BaseModel):
    title: str
    content: str


@app.get("/")
def home():
    return PostDatbase.all_post()


@app.post("/createpost")
def create(post_data: Post, res: Response):
    res.status_code = status.HTTP_201_CREATED
    return PostDatbase.add_post(post_data.title, content=post_data.content)

@app.get('/{id}')
def retrieve(id: int): 
    data = PostDatbase.retrieve_post(id)
    if not data: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return data

@app.delete("/delete/{id}")
def delete(id: int): 
    if PostDatbase.delete_post(id):
        return {"message": "deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.patch('/updatepost/{id}')
def update(id: int, title: Annotated[str | None, Body()] = None, content: Annotated[str|None, Body()]=None):
    data = PostDatbase.update_post(id, title=title, content=content)
    if data: 
        return data
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
