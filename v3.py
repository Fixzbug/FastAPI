from enum import Enum
class Tags(Enum):
    Main = "Main"
    Product = "Product"
    User = "User"
    
 
@app.get("/", tags=[Tags.Main])
@app.get("/products/{product_id}", tags=[Tags.Product])
@app.post("/products/", tags=[Tags.Product])
@app.put("/users/{user_id}", tags=[Tags.User])