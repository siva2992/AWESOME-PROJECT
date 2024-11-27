from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    price: float
    is_offer: bool = None
    
class Book(BaseModel):
    book_name: str
    book_price: float


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{items_id}")
def save_item(item_id:int, item:Item):
    return{"item_name":item.pr, "item_id":item_id}



# /books   GET	      Get a list of all books

@app.get("/books")
def get_books():
    return {"List of book"}


# /books   POST         Create a book

@app.post("/books")
def create_book(book: Book):
    return {book.book_name, book.book_price}

# /book/{book_id} PATCH Update a book
@app.patch("/book/{book_id}")
def update_book(book_id: int):
    return book_id

# /book/{book_id} DELETE Delete a book
