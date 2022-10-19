import json
import pydantic
from typing import List, Optional


class Book(pydantic.BaseModel):
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]


def main() -> None:
    with open("Desktop/Programming/Learn/Python/modules/pydantic/example.json") as f:
        data = json.load(f)
        books: List[Book] = [Book(**item) for item in data]
        print(books[0].title)
        
        
if __name__ == "__main__":
    main()