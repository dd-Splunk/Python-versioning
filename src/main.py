from fastapi import FastAPI

from src.version import __version__

# Minimal setup

app = FastAPI(
    version=__version__,
)
