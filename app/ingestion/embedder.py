from openai import OpenAI

from app.config import settings

client = OpenAI(api_key=settings.openai_api_key)


class OpenAIEmbedder:
    model = "text-embedding-3-small"

    def embed(self, texts: list[str]) -> list[list[float]]:
        resp = client.embeddings.create(model=self.model, input=texts)
        return [d.embedding for d in resp.data]
