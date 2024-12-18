from datetime import datetime
from typing import List, Dict, Any
from search_module import search_entries
from contextual_module import contextual_search

def run_cli_interface(news_data: List[Dict[str, Any]]) -> None:
    print("Welcome to the News Search System!")

    user_history = []
    user_location = ""

    while True:
        mode = input("\nChoose search mode (1: Basic, 2: Contextual, 'exit' to quit): ").strip()
        if mode.lower() == 'exit':
            print("\nThank you for using the system. Goodbye!")
            break

        if mode not in ['1', '2']:
            print("Invalid option. Please choose either 1 (Basic) or 2 (Contextual).")
            continue

        if mode == '2' and not user_location:
            user_location = input("\nEnter your location (e.g., Kyiv, Lviv, Odessa): ").strip()

        query = input("\nEnter your search query: ").strip()

        if mode == '1':
            results = search_entries(query, news_data)
        else:
            current_date = datetime.now()
            results = contextual_search(query, news_data, user_history, user_location, current_date)
            user_history.append(query)

        print("\nTop results:")
        if results:
            for i, result in enumerate(results[:5], start=1):  # Display top 5 results
                print(f"{i}. [{result['category']}] {result['title']} "
                      f"({result['date']}, {result['location']}) - Relevance: {result['relevance']:.2f}")
                print(f"   Summary: {result['summary']}")
                print(f"   Content: {result['content']}\n")
        else:
            print("No results found.")
