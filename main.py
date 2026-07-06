from fastapi import FastAPI

app = FastAPI(title="学习 Agent 后端")


@app.get("/health")
def health():
    return {"status": "ok"}