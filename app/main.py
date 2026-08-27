from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from app.api.routes import router

app = FastAPI(title="arXiv Research Assistant", version="0.1.0")
app.include_router(router)


@app.get("/scalar", include_in_schema=False)
def scalar_docs():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title=app.title)
