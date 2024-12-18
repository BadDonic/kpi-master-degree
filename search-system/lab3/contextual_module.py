from difflib import SequenceMatcher
from datetime import datetime
from typing import List, Dict, Any, Optional
from search_module import normalize_text

def compute_contextual_score(
    cleaned_query: str,
    entry: Dict[str, Any],
    user_history: List[str],
    user_location: Optional[str],
    current_date: datetime
) -> float:

    # Extract and preprocess text fields
    title_text = normalize_text(entry["title"])
    summary_text = normalize_text(entry["summary"])
    content_text = normalize_text(entry["content"])

    # Exact matches
    exact_title_match = 5 if cleaned_query in title_text else 0
    exact_summary_match = 3 if cleaned_query in summary_text else 0
    exact_content_match = 1 if cleaned_query in content_text else 0

    # Partial matches via sequence similarity
    partial_score = 0.0
    partial_score += SequenceMatcher(None, cleaned_query, title_text).ratio() * 5
    partial_score += SequenceMatcher(None, cleaned_query, summary_text).ratio() * 3
    partial_score += SequenceMatcher(None, cleaned_query, content_text).ratio() * 1

    # User history influence
    history_bonus = sum(¡¡
        2 for past_query in user_history
        if past_query in title_text or past_query in content_text
    )

    # Location relevance
    location_bonus = 3 if user_location and user_location == entry.get("location", "") else 0

    # Date relevance
    news_date = datetime.strptime(entry["date"], "%Y-%m-%d")
    date_difference = abs((current_date - news_date).days)
    date_bonus = 3 if date_difference <= 3 else 0

    # Total relevance score
    total_score = (
        exact_title_match + exact_summary_match + exact_content_match +
        partial_score + history_bonus + location_bonus + date_bonus
    )
    return total_score

def contextual_search(
    query: str,
    data: List[Dict[str, Any]],
    user_history: Optional[List[str]] = None,
    user_location: Optional[str] = None,
    current_date: Optional[datetime] = None
) -> List[Dict[str, Any]]:
    if user_history is None:
        user_history = []
    if current_date is None:
        current_date = datetime.now()

    cleaned_query = normalize_text(query)
    matched_results = []

    for item in data:
        relevance = compute_contextual_score(cleaned_query, item, user_history, user_location, current_date)
        if relevance > 0:
            matched_results.append({
                "category": item["category"],
                "title": item["title"],
                "date": item["date"],
                "location": item["location"],
                "summary": item["summary"],
                "content": item["content"],
                "relevance": relevance
            })

    matched_results.sort(key=lambda x: x["relevance"], reverse=True)
    return matched_results
