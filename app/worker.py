from celery import Celery

from app.config import settings

celery_app = Celery("arxiv_rag", broker=settings.redis_url, backend=settings.redis_url)


@celery_app.task
def ping() -> str:
    return "pong"
