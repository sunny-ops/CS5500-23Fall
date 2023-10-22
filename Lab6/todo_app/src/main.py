from fastapi import FastAPI, Body

app = FastAPI()

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
def get_api_path_query(path_param: str, title:str):
    return {"msg": {"path": path_param, "title":title}}
    # return {"msg": path_param + title}


@app.post("/books/create_book")
def first_apiV4(new_book=Body()):
    print(new_book)
    return {"msg": new_book}


