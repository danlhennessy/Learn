from dataclasses import dataclass

@dataclass
class country:
    capital: str
    
Nigeria= country(capital = "Abuja")

print(Nigeria.capital)