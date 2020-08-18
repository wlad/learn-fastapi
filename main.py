# 1. import FastAPI
# 2. create an app (FastAPI) instance
# 3. wirte a path operation decorator (like @app.get("/"))
# 4. define path operation function (like def or async def root)
# 5. return the contente
# 6. run dev server (uvicorn main:app --reload)


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello WLAD"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/switch-light/{switch}")
async def switch_light(switch: str):
    return {"light status": f"the light is {switch}"}
