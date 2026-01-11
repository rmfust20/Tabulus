from sqlmodel import Field, Session, SQLModel, create_engine, select


class BoardGameDesignerLink(SQLModel, table=True):
    board_game_id: int = Field(foreign_key="boardgame.id", primary_key=True)
    designer_id: int = Field(foreign_key="boardgamedesigner.id", primary_key=True)