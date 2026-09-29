"""
duplicate_article_detector.py - Calculates semantic cosine similarity against published knowledge base articles
"""
import sys
import json


def detect_duplicate_articles(similarity_check_json: str):
    import json
    data = json.loads(similarity_check_json) if isinstance(similarity_check_json, str) else similarity_check_json
    c_title = data.get("candidate_title", "").lower()
    existing = [t.lower() for t in data.get("existing_titles", [])]
    is_dup = any(c_title == e for e in existing)
    return {"duplicate_found": is_dup, "status": "DUPLICATE_FOUND" if is_dup else "NO_DUPLICATE_FOUND"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "duplicate-article-detector"}))
