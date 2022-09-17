import json
import pydantic
from typing import List

class Book(pydantic.BaseModel):
    
    ID: str
    SortAs: str
    GlossTerm: str
    Acronym: str
    Abbrev: str


def main() -> None:
    with open("Desktop/Programming/Learn/Python/modules/pydantic/example.json") as f:
        data = json.load(f)
        glossentry = data['glossary']['GlossDiv']['GlossList']['GlossEntry']
        books: List[Book] = [Book(**item) for item in glossentry]
        print(data['glossary']['GlossDiv']['GlossList']['GlossEntry'])
        
        
if __name__ == "__main__":
    main()