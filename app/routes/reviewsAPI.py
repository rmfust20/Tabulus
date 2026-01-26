from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from app.connection import SessionDep
from fastapi import APIRouter
from sqlmodel import Field, Session, SQLModel, create_engine, select
from app.models import Review, UserBoardGame
from app.services import getBoardGameByName, reviewsService
from app.services.userService import get_current_user


router = APIRouter(
    prefix="/reviews",
)

@router.get("/getBoardGames/{board_game_id}", response_model=list[Review])
def read_reviews_by_board_game_name(board_game_id, session: SessionDep):     #consider how this is ordered later -> by date created desc? popularity?
    statement = select(Review).where(Review.board_game_id == board_game_id).order_by(Review.id).limit(25)

    reviews = session.exec(statement).all()
    
    return reviews

@router.post("/postReview", response_model=Review)
def create_review_for_board_game(review: Review, session: SessionDep, 
                                 user: UserBoardGame = Depends(get_current_user)): 
    #do need to ensure that the userID is the same as the authenticated user
    if review.user_id != user.id:
        raise HTTPException(403, "Cannot create review for another user")
    return reviewsService.insert_review_for_board_game(review, session)





    