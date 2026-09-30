book = {
    "title": "Eleanor and Park",
    "author": "Rainbow Rowell",
    "pages": 300,
    "available": False
}

print(f'Tittel: {book["title"]} og Forfatter: {book["author"]}.')

book["available"] = True
book["year"] = 2018

print(book)