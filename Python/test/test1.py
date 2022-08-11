from dataclasses import dataclass
@dataclass
class person:
    n: str = "Default"
    age: int = 22
    
fred = person("Fred", 45)

print(fred.age)