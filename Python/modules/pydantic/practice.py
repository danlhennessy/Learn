import json
import pydantic


def main() -> None:
    with open("Desktop/Programming/Learn/Python/modules/pydantic/example.json") as f:
        data = json.load(f)
        print(data['glossary']['title'])
        
        
if __name__ == "__main__":
    main()