from fastapi import FastAPI
from src.orchestrator import run

app = FastAPI()

@app.get("/")
def root():
    return run({"task": "demo"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
