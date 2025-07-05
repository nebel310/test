from fastapi import FastAPI
import uvicorn




app = FastAPI()

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