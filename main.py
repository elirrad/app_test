from fastapi import Depends, FastAPI
from pydantic import BaseModel
from models import User, get_db
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()


# creation de table
# CREATE TABLE userss (,
#     nom TEXT NOT NULL,
#     prenom TEXT NOT NULL,
#     age INT NOT NULL,
# );
class UserModel(BaseModel):
    name: str
    email: str
    cadeau: bool


@app.post("/users/")
def create_user(user_request: UserModel, db: Session = Depends(get_db)):
    """
    # Créer un utilisateur dans la base de données
    ### il cree grace a la methode post
    les paramettres sont `name` et `email`
    """
    # verifier si l'utilisateur existe deja
    user = db.query(User).filter(User.email == user_request.email).first()
    if user:
        return {"error": "User already exists"}
    user = User(name=user_request.name, email=user_request.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User has been created successfully"}


@app.get("/users/")
def read_users(db=Depends(get_db)):
    """
    # Lire tous les utilisateurs dans la base de données
    ### il lit grace a la methode get
    """
    users = db.query(User).all()
    return users


@app.get("/users/{email}")
def get_user_by_email(email: str, db=Depends(get_db)):
    """
    # Lire un utilisateur par e-mail
    ### il lit grace a la methode get
    ### on filtre par email
    """
    user = db.query(User).filter(User.email == email).first()
    return user


@app.put("/users/{email}")
def update_user_by_email(
    email: str, user_request: UserModel, db: Session = Depends(get_db)
):
    # Mettre à jour un utilisateur dans la base de données
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        return {"error": "User not found"}
    user.name = user_request.name
    if user_request.email != user.email:
        return {"error": "Email cannot be updated"}
    db.commit()
    db.refresh(user)
    return {"message": "User has been updated successfully"}


@app.delete("/users/{email}")
def delete_user_by_email(email: str, db: Session = Depends(get_db)):
    """
    # Supprimer un utilisateur par e-mail
    ### il supprime grace a la methode delete
    ### on filtre par email
    """
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        return {"error": "User not found"}
    db.delete(user)
    db.commit()
    return {"message": "User has been deleted successfully"}


@app.post("/users/{email}/offre_cadeau")
def create_offre_cadeau(email: str, db: Session = Depends(get_db)):
    """
    # Créer une offre cadeau pour un utilisateur
    ### il cree grace a la methode post
    ### on filtre par email
    """
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        return {"error": "User not found"}
    user.cadeau = True
    db.commit()
    db.refresh(user)
    return {"message": "Offre cadeau créée avec succès"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
