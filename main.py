# 1.从fastapi包里导入FastAPI，用于构建FastAPI应用程序
from fastapi import FastAPI

# 2.初始化FastAPI应用程序实例
app = FastAPI(title="学习 Agent 后端")


# 3.定义一个访问接口，每当访问这个接口时，返回一个固定的信息
@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ping")
def ping():
    return {"message":"pong"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"hello,{name}"}


@app.get("/items")
def get_items(limit: int=10):
    return {
        "limit": limit,
        "items":[f"item-{i}" for i in range(1,limit+1)]
    }