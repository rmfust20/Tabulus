from sqlmodel import Field, Session, SQLModel, create_engine, select


class BoardGameCategoryLink(SQLModel, table=True):
    board_game_id: int = Field(foreign_key="boardgame.id", primary_key=True)
    category_id: int = Field(foreign_key="boardgamecategory.id", primary_key=True)
