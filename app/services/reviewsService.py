


from app.connection import SessionDep
from app.models import Review



def insert_review_for_board_game(review: Review, session: SessionDep) -> Review:
    session.add(review)
    session.commit()
    session.refresh(review)
    
    return review



