from fastapi import FastAPI

from app.version import __version__

# Minimal setup

app = FastAPI(
    version=__version__,
)
