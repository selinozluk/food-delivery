from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Yeni eklediğim endpoint
@app.get("/orders/")
def read_orders():
    return {"orders": "This will return a list of orders"}
