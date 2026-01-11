from app.models import UserBoardGame, UserBoardGameCreate, UserBoardGamePublic, UserBoardGameUpdate
from fastapi import APIRouter
from app.connection import SessionDep

router = APIRouter(
    prefix="/users",
)

@router.post("/create", response_model=UserBoardGamePublic)
def create_user(user: UserBoardGameCreate, session: SessionDep):
    db_user = UserBoardGame.model_validate(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user