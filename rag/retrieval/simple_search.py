from pathlib import Path


DOCUMENT_DIR = Path("rag/documents")


def search_documents(query: str) -> list[dict]:
    """Search local text documents using simple keyword overlap."""

    query_words = set(query.lower().split())
    results = []

    for path in DOCUMENT_DIR.glob("*.txt"):
        text = path.read_text(encoding="utf-8")
        text_words = set(text.lower().split())

        score = len(query_words.intersection(text_words))

        if score > 0:
            results.append(
                {
                    "document": path.name,
                    "score": score,
                    "content": text,
                }
            )

    return sorted(
        results,
        key=lambda item: item["score"],
        reverse=True,
    )
