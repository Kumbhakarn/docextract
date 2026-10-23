"""Liveness endpoint."""

from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    """Body returned by ``GET /health``."""

    status: Literal["ok"]


@router.get("/health")
def get_health() -> HealthResponse:
    """Report that the process is up and serving requests.

    Liveness only: it touches no dependencies, so it stays cheap and never
    fails because something downstream is slow.
    """
    return HealthResponse(status="ok")
