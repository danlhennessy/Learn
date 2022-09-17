import json



def main() -> None:
    with open("Desktop/Programming/Learn/Python/modules/pydantic/example.json") as f:
        data = json.load(f)
        print(data[0]['glossary']['title'])
        
        
if __name__ == "__main__":
    main()