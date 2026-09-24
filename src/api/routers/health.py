from fastapi import APIRouter

health_router = APIRouter()

@health_router.get("/health",tags=["Health"])
def Health() -> dict[str, str]:
    """Checks server status"""
    return {"status": "active"}