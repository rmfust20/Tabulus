from sqlmodel import Field, Session, SQLModel, create_engine, select


class BoardGame(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(index=True)
    thumbnail: str | None = Field(default=None)
    play_time: int | None = Field(default=None)
    min_players: int | None = Field(default=None)
    max_players: int | None = Field(default=None)
    year_published: int | None = Field(default=None)
    description: str | None = Field(default=None)
    min_age: int | None = Field(default=None)
    image: str | None = Field(default=None)