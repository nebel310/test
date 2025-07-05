from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx
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

@app.get("/ask_serv2")
async def ask_b():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://serv2:3002/hello")  # Для Docker. Локально: "http://127.0.0.1:8001/hello"
    return {"response_from_serv2": response.json()}


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        #reload=True,
        port=3001,
        host='0.0.0.0'
    )