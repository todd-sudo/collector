from fastapi import FastAPI

from routes import routes
from settings import settings


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(routes, prefix=settings.API_V1_STR)
