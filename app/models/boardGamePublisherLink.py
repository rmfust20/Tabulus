from sqlmodel import Field, Session, SQLModel, create_engine, select


class BoardGamePublisherLink(SQLModel, table=True):
    board_game_id: int = Field(foreign_key="boardgame.id",primary_key=True)
    publisher_id: int = Field(foreign_key="publisher.id",primary_key=True)
    
    
