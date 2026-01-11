from sqlmodel import Field, Session, SQLModel, create_engine, select


class BoardGameMechanicLink(SQLModel, table=True):
    board_game_id: int = Field(foreign_key="boardgame.id", primary_key=True)
    mechanic_id: int = Field(foreign_key="boardgamemechanic.id", primary_key=True)
