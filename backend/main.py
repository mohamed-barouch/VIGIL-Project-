from fastapi import FastAPI

app = FastAPI(title="Vigil")
PRODUCTS = [
    {"id": 1,"name": "Keyboard", "price": 49.9},
    {"id": 2,"name": "Mouse", "price": 19.9},
    {"id": 3,"name": "Monitor", "price": 189.0},
]

@app.get("/health")
def health():
    return{"status": "ok"}
@app.get("/products")
def products():
    return PRODUCTS
