from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from server.routes.graphology import router as GraphologyRouter

app = FastAPI(
    title="Graphology Docs",
    description="This is the documentation for Graphology's API.",
    version="1.0",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    docs_url="/graphology_docs",
    redoc_url=None,
    basePath="/v1",
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"],
)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"graphology server is running"}


app.include_router(GraphologyRouter, tags=["Graphology-service"], prefix="/v1")