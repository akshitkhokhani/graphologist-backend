import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "server.app:app",
        host="0.0.0.0",
        port=8088,
        lifespan="on",
        workers=3,
        reload=True,
    )
