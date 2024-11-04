from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["Main"])
async def root():
    return {"message": "Hello World"}

@app.get("/products/{product_id}", tags=["Product"])
async def get_product(product_id: int):
    return {"product_id": product_id}

@app.post("/products/", tags=["Product"])
async def create_product(product: dict):
    return {"product": product}

@app.put("/users/{user_id}", tags=["User"])
async def update_user(user_id: int):
    return {"user_id": user_id}