from fastapi import FastAPI

app = FastAPI(
    title="PokeMMO Market Engine",
    description="API de análise e previsão de mercado para economia do PokeMMO",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"status": "online", "project": "PokeMMO Market Engine"}