
print("salut elimeleh le meilleur des petits freres")
from fastapi import FastAPI, APIRouter

app = FastAPI()

#connexion a la DB
import sqlite3
connection = sqlite3.connect('DB.db')

CREATE TABLE users (,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    age INT NOT NULL,
);




users=[{"name":"elimeleh","age":18},{"name":"eli","age":18}]


@app.get("/")
def hello(name):
    return {"message": "Hello "+name}
@app.get("/age")
def get_age(age):
    return{"age":age}
@app.get("/user")
def get_user(name):
    for user in users:
        if name==user["name"]:
            return user

    return{
        "error":"not fond",
    }


if __name__ == "__main__":
    app.include_router(app)
    import uvicorn

    uvicorn.run(app)