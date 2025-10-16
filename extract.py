import requests

def extract_data():
    """Extract data from a free public API (JSONPlaceholder)."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
