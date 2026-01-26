from sqlmodel import Field, Session, SQLModel, create_engine, select

class UserBoardGameBase(SQLModel):
    username: str = Field(index=True)
    email: str = Field(index = True)

class UserBoardGame(UserBoardGameBase,table=True):
    id: int | None = Field(default=None, primary_key=True)
    password_hash : str

class UserBoardGamePublic(UserBoardGameBase):
    id: int

class UserBoardGameCreate(UserBoardGameBase):
    password : str

class UserBoardGameUpdate(UserBoardGameBase):
    username: str | None = None
    email: str | None = None
    password: str | None = None

