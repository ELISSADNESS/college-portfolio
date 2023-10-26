from fastapi import FastAPI

from .config.db import Base

from .config.db import engine

from .routers import works, authors

app = FastAPI(
    title = "College Portfolio API",
    docs_url = "/documentation",
    redoc_url = None
)

Base.metadata.create_all(bind=engine)
app.include_router(works.router)
app.include_router(authors.router)
