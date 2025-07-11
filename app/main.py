from fastapi import FastAPI
from .routes import users

app = FastAPI()
app.include_router(users.router)

@app.get('/')
def home():
    return {'Hello': 'World'}

@app.get('/about')
def about():
    return {'Ab': 'out'}
