import urllib.request
import json

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