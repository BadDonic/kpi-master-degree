import re
from difflib import SequenceMatcher
from typing import List, Dict, Any

def normalize_text(original_text: str) -> str:
    return re.sub(r'[^\w\s]', '', original_text.lower())

def compute_score(input_query: str, entry: Dict[str, Any]) -> float:
    processed_query = normalize_text(input_query)
    processed_title = normalize_text(entry['title'])
    processed_summary = normalize_text(entry['summary'])
    processed_content = normalize_text(entry['content'])

    query_terms = processed_query.split()

    title_keyword_hits = sum(processed_title.count(term) for term in query_terms)
    summary_keyword_hits = sum(processed_summary.count(term) for term in query_terms)
    content_keyword_hits = sum(processed_content.count(term) for term in query_terms)

    partial_score = 0.0
    partial_score += SequenceMatcher(None, processed_query, processed_title).ratio() * 5
    partial_score += SequenceMatcher(None, processed_query, processed_summary).ratio() * 3
    partial_score += SequenceMatcher(None, processed_query, processed_content).ratio() * 1

    total_score = (
        (title_keyword_hits * 3) +
        (summary_keyword_hits * 2) +
        content_keyword_hits +
        partial_score
    )

    return total_score

def search_entries(input_query: str, entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    normalized_query = normalize_text(input_query)
    matched_results = []

    for single_entry in entries:
        score = compute_score(normalized_query, single_entry)
        if score > 0:
            matched_results.append({
                "category": single_entry["category"],
                "title": single_entry["title"],
                "date": single_entry["date"],
                "location": single_entry["location"],
                "summary": single_entry["summary"],
                "content": single_entry["content"],
                "relevance": score
            })

    matched_results.sort(key=lambda x: x["relevance"], reverse=True)
    return matched_results
