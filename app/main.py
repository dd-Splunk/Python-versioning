from app.version import __version__

app = FastAPI(
    version=__version__,
)