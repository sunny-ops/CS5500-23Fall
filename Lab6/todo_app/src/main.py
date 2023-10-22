from fastapi import FastAPI, Body

app = FastAPI()

books_db = {
    1: {"title": "Book 1", "author": "Author 1"},
    2: {"title": "Book 2", "author": "Author 2"},
}

@app.get("/api")
def get_api():
    return {"msg":"hello_worldAAA"}

@app.get("/books/{path_param}")
def get_api_path(path_param: str):
    return {"msg": path_param}

@app.get("/books/")
def get_api_query(title:str):
    return {"msg": title}

@app.get("/mybooks/{path_param}/")
def get_api_path_query(path_param: str, query_param:str):
    return {"msg": {"path": path_param, "query":query_param}}
    # return {"msg": path_param + title}


@app.post("/books/create_book")
def first_apiV4(new_book=Body()):
    print(new_book)
    return {"msg": new_book}

@app.put("/books/update_book/{book_id}")
def update_book(book_id: int, book_data=Body()):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not Found!")
    # updated_book = book_data.dict()
    books_db[book_id] = book_data
    print(book_data)
    return {"meg": book_data}

@app.delete("/books/delete_book/{book_id}")
def delete_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not Found!")
    book_data = books_db[book_id]
    del books_db[book_id]
    print(book_data)
    return {"meg": book_data}


