from sqlmodel import Field, Session, SQLModel, create_engine, select


class BoardGameDesigner(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(index=True)