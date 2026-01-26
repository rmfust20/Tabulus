from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import datetime

class RefreshToken(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="userboardgame.id", index=True)
    token_hash : str = Field(index=True)
    expires_at: datetime
    revoked_at: datetime | None = Field(default=None)
    