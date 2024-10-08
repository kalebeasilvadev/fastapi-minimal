from fastapi import FastAPI
from app.api.router import router

app = FastAPI()


app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Bem-vindo à API!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
