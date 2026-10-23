"""FastAPI application entry point."""

from fastapi import FastAPI

from docextract.api import health


def create_app() -> FastAPI:
    """Build the application with all routers registered."""
    app = FastAPI(title="docextract")
    app.include_router(health.router)
    return app


app = create_app()
