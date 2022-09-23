from dataclasses import dataclass

@dataclass
class country:
    capital: str
    
africa = country(capital = "Zimb")

print(africa.capital)