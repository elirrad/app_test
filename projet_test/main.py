from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter()


@router.get("/")
def hello():
    return {"message": "Hello World"}


if __name__ == "__main__":
    app.include_router(router)
    import uvicorn

    uvicorn.run(app)
