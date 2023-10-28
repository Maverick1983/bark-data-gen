import random

import requests


books = [
    'https://www.gutenberg.org/ebooks/57822.txt.utf-8',
    'https://www.gutenberg.org/ebooks/27608.txt.utf-8',
    'https://www.gutenberg.org/ebooks/42436.txt.utf-8',
    'https://www.gutenberg.org/ebooks/26166.txt.utf-8'
]

allowed_chars = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=\"\':;[]{}/<>,.`~\n\\'


def download_book(book):
    return requests.get(book).content.decode('utf-8')


def filter_data(data):
    print('Filtering data')
    return ''.join([char for char in data if char in allowed_chars])


def load_books():
    text_data = []
    print(f'Loading {len(books)} books into ram')
    for book in books:
        text_data.append(filter_data(str(download_book(book))))
    print('Loaded books')
    return ' '.join(text_data)


def random_split_chunk(data, size=14):
    data = data.split(' ')
    index = random.randrange(0, len(data))
    return ' '.join(data[index:index+size])
