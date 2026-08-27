from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/hello")
def hello(name: str = "world") -> dict[str, str]:
    return {"message": f"hello, {name}"}
