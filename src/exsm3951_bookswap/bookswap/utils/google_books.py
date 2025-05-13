import urllib.request
import json
from urllib.parse import quote_plus

def get_cover_image(title, author=None):
    query = f'intitle:{title}'
    if author:
        query += f'+inauthor:{author}'
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=1'

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            return data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
    except Exception:
        return None


def get_books_data(query, max_results=40):
    encoded_query = quote_plus(query)
    url = f"https://www.googleapis.com/books/v1/volumes?q={encoded_query}&maxResults={max_results}"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            books = []

            for item in data.get("items", []):
                volume = item.get("volumeInfo", {})

                books.append({
                    "isbn": extract_isbn(volume),
                    "title": volume.get("title", "Unknown Title"),
                    "author": ", ".join(volume.get("authors", ["Unknown Author"])),
                    "genre": volume.get("categories", ["General"])[0],
                    "description": volume.get("description", "No description available."),
                    "pub_date": volume.get("publishedDate", "1900-01-01"),
                    "language": volume.get("language", "en"),
                    "image_url": volume.get("imageLinks", {}).get("thumbnail"),
                })

            return books

    except Exception as e:
        print("Google Books API error:", e)
        return []

def extract_isbn(volume):
    """Try to extract a valid ISBN, fallback to empty string."""
    identifiers = volume.get("industryIdentifiers", [])
    for id_entry in identifiers:
        if id_entry.get("type") in ["ISBN_13", "ISBN_10"]:
            return id_entry.get("identifier")
    return ""