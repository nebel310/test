from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Для разработки. В продакшене укажите конкретные домены
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": 200}

@app.get("/hello")
async def hello():
    return {"message": "Hello from Service 2!"}


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        #reload=True,
        port=3002,
        host='0.0.0.0'
    )