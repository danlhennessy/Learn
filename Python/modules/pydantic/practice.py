import json
import pydantic

class Book(pydantic.BaseModel):
    
    ID: str
    SortAs: str
    GlossTerm: str
    Acronym: str
    Abbrev: str


def main() -> None:
    with open("Desktop/Programming/Learn/Python/modules/pydantic/example.json") as f:
        data = json.load(f)
        print(data['glossary']['title'])
        
        
if __name__ == "__main__":
    main()