import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.interface.api.main:app", host="localhost", port=8000, reload=True) 