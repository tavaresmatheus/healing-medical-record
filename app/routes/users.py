from fastapi import APIRouter

router = APIRouter(prefix='/users')

@router.get('/me')
def get_me():
    return {'me': 'yes'}
