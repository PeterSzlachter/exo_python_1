import re
import string
from tinydb import TinyDB, where
from pathlib import Path

class User:
    
    db = TinyDB(Path(__file__).resolve().parent / "db.json", indent=4,ensure_ascii=True)
    
    def __init__(self, first_name:str,last_name:str,phone_number:str="",address:str=""):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
    
    def __repr__(self) -> str:
        return f"User({self.first_name} {self.last_name})"
    def __str__(self) -> str:
        return f"Prénom: {self.first_name}\nNom: {self.last_name}\nTéléphone: {self.phone_number}\nAdresse: {self.address}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def db_instance(self):
        return User.db.get((where('first_name') == self.first_name) & (where('last_name') == self.last_name))  # type: ignore
    
    def _check_phone_number(self):
        phone_number = re.sub(r"[+()\s]*", "", self.phone_number)
        if len(phone_number) < 10 or not phone_number.isdigit():
            raise ValueError(f"Numéro de téléphone {self.phone_number} invalide")

    def _check_names(self):
        if not (self.first_name and self.last_name):
            raise ValueError("Le prénom et le nom de famille ne peuvent pas être vides")
        special_char = string.punctuation + string.digits
        print(special_char)
        
        for character in self.first_name + self.last_name:
            if character in special_char.replace("-",""):
                raise ValueError(f"Nom invalide {self.full_name}")
    
    def _checks(self):
        self._check_phone_number()
        self._check_names()
    
    def exists(self):
        return bool(self.db_instance)
    
    def delete(self) -> list[int]:
        if self.exists():
            return User.db.remove(doc_ids=[self.db_instance.doc_id])
        return []
        
    def save(self, validate_data:bool = False) -> int:
        if validate_data:
            self._checks()
            
        return User.db.insert(self.__dict__)
    
def get_all_users():
    return [User(**user) for user in User.db.all()]
    # for user in User.db.all():
    #     each_user = User(**user)
    #     print(each_user.full_name)
        
        
        
if __name__ == "__main__":
    monik = User("Luc", "Moreno")
    print(monik.delete())