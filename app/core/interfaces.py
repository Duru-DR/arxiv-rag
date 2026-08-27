from typing import Protocol


class Embedder(Protocol):
    def embed(self, texts: list[str]) -> list[list[float]]: ...


class Retriever(Protocol):
    def retrieve(self, query: str, top_k: int) -> list[dict]: ...


class Reranker(Protocol):
    def rerank(self, query: str, candidates: list[dict]) -> list[dict]: ...


class Generator(Protocol):
    def generate(self, question: str, context: list[dict]) -> dict: ...
