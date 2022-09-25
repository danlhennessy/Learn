from dataclasses import dataclass

@dataclass
class country:
    capital: str
    pop: int = 20_000
    
Nigeria= country(capital = "Abuja")

print(Nigeria.capital)

print(Nigeria.pop)