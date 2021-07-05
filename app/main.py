from decouple import config
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes.api import router as api_router


def get_application() -> FastAPI:
    application = FastAPI(title=config("PROJECT_NAME"), debug=config("DEBUG"))

    application.add_middleware(
        CORSMiddleware,
        allow_origins= ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_router, prefix="/api")
    return application


app = get_application()
