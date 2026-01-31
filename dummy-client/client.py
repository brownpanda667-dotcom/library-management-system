import time
import requests
import random

API_URL = "http://app:8080/api/books"

TITLES = ["Wings of Fire", "The Guide", "Train to Pakistan", "The God of Small Things", "Malgudi Days"]
AUTHORS = ["A.P.J. Abdul Kalam", "R.K. Narayan", "Khushwant Singh", "Arundhati Roy", "R.K. Narayan"]

def add_book():
    book = {
        "title": random.choice(TITLES),
        "author": random.choice(AUTHORS),
        "isbn": str(random.randint(1000000000, 9999999999))
    }
    try:
        response = requests.post(API_URL, json=book)
        if response.status_code == 200:
            print(f"Added: {book['title']}")
        else:
            print(f"Failed to add book: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Dummy client started. Waiting for app to be ready...")
    time.sleep(20) # Wait for app to boot
    while True:
        add_book()
        time.sleep(10)
