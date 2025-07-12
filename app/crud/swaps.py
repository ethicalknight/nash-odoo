from ..models import db, SwapRequest

def get_swaps_for_user(user_id):
    return SwapRequest.query.filter(
        (SwapRequest.from_user == user_id) | (SwapRequest.to_user == user_id)
    ).all()

def update_swap_status(swap_id, status):
    swap = SwapRequest.query.get(swap_id)
    if not swap:
        return None
    swap.status = status
    db.session.commit()
    return swap
