from fastapi import APIRouter

router = APIRouter(prefix='/api/users')

@router.get('/me')
def get_me():
    return {'me': 'yes'}
