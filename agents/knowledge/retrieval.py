from pathlib import Path
import re


DOCUMENT_DIR = Path(__file__).resolve().parent / "documents"


STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "how",
    "i",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "this",
    "to",
    "what",
    "when",
    "where",
    "which",
    "who",
    "with",
}


def tokenize(text: str) -> set[str]:
    words = re.findall(r"[a-zA-Z0-9]+", text.lower())

    return {
        word
        for word in words
        if word not in STOP_WORDS and len(word) > 1
    }


def search_documents(query: str) -> list[dict]:
    """Search NovaRetail documents using keyword overlap."""

    query_words = tokenize(query)
    results = []

    if not DOCUMENT_DIR.exists():
        return []

    for path in DOCUMENT_DIR.glob("*.txt"):
        text = path.read_text(encoding="utf-8")

        text_words = tokenize(text)
        matched_words = query_words.intersection(text_words)

        score = len(matched_words)

        if score > 0:
            results.append(
                {
                    "document": path.name,
                    "score": score,
                    "matched_terms": sorted(matched_words),
                    "content": text,
                }
            )

    return sorted(
        results,
        key=lambda item: item["score"],
        reverse=True,
    )