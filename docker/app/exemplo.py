from fastapi import FastAPI


app = FastAPI()

@app.get("/api") 
async def root():
    return {"message": " você está indo muito bem com a FastAPI PARABÉNS..."}

@app.get("/api/{name}")
async def get_user(name):
    return {
        "name": name,
        "message": f"Hello, {name} from FastAPI."}
