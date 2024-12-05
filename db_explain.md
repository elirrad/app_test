### DB connection
```
DATABASE_URL = "sqlite:///./task.db"
```
### Tables 
- ex: user 
```
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class User(Base):
```

### Column
- ex name , email
```
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

```

## Requet
|              | DB lng | Http lng |
|--------------|--------|----------|
| insertion    | Create | post     |
| recuperation | Read   | get      |
| modification | Update | put      |
| suppression  | Delete | delete   |
