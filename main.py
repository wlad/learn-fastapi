# 1. import FastAPI
# 2. create an app (FastAPI) instance
# 3. wirte a path operation decorator (like @app.get("/"))
# 4. define path operation function (like def or async def root)
# 5. return the contente
# 6. run dev server (uvicorn main:app --reload)


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "hello WLAD"}
