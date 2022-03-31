from dataclasses import dataclass #classes de données depuis Python 3.7
from typing import ClassVar #pour faire des attributs de classe

@dataclass
class User:
    first_name: str
    last_name: str #attributs d'instance
    c: ClassVar[int] = 10 #attributs de classe valeur par défaut 10
    
    # def __post_init__(self):
    #     self.full_name = f"{self.first_name} {self.last_name}"
    
#équivalent
# class User:
#     def __init__(self,first_name,last_name):
#         self.first_name = first_name
#         self.last_name = last_name

Peter = User(first_name="Peter",last_name="S")
print(repr(Peter))
print(Peter.__dict__)
# print(User.__dict__)
