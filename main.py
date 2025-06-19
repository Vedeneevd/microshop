from fastapi import FastAPI

import uvicorn

app = FastAPI()


@app.get('/')
def hello_index():
    return {
        "message": "hello index",
    }


@app.get('/hello/')
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}!"}


app.get("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)