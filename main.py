from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./task.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()
# creation de table
# CREATE TABLE userss (,
#     nom TEXT NOT NULL,
#     prenom TEXT NOT NULL,
#     age INT NOT NULL,
# );


users = [{"name": "elimeleh", "age": 18}, {"name": "eli", "age": 18}]


@app.get("/")
def hello(name):
    return {"message": "Hello " + name}


@app.get("/age")
def get_age(age):
    return {"age": age}


@app.get("/user")
def get_user(name):
    for user in users:
        if name == user["name"]:
            return user

    return {
        "error": "not fond",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
