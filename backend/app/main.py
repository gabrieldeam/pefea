from fastapi import FastAPI
from app.routers import example
from app.database import engine, Base
from app.models.example import Example  # Importe o modelo corretamente

app = FastAPI()

# Incluindo as rotas
app.include_router(example.router)

# Cria todas as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

# Comando para rodar o servidor:
# uvicorn app.main:app --reload
