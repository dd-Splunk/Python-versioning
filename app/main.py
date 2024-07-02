from fastapi import FastAPI

from app.version import __version__

# New feature

app = FastAPI(
    version=__version__,
)
