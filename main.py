from typing import Union
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def read_root():
    return FileResponse("html/main.html")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/{css_path}/{css_name}.css")
def read_css(css_path:str, css_name: str):
    css = "css/" + css_path + "/" + css_name + ".css"
    return FileResponse(css)
