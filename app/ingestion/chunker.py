def chunk_text(text: str, words_per_chunk: int = 200) -> list[str]:
    words = text.split()
    return [" ".join([i, i + words_per_chunk]) for i in range(0, len(words), words_per_chunk)]
