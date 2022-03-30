"""module generateur d'utilisateur"""
import faker
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(level=logging.DEBUG,
                    filename=BASE_DIR/"user.log",
                    filemode="w",
                    format='%(asctime)s - %(levelname)s - %(message)s')

fake = faker.Faker()

def get_user() -> str:
    """get_user
    
    Returns:
        str: retourne un utilisateur généré aléatoirement avec Faker
    """
    logging.info("Generation d'un utilisateur.")
    user = f"{fake.first_name()} {fake.last_name()}"
    return user
    
def get_users(number_wanted:int):
    """get_users

    Args:
        number_wanted (int): nombre d'utilisateur voluptatum

    Returns:
        list[str]: liste d'utilisateur généré par la fonction get_user
    """
    logging.info(f"Generation de {number_wanted} utilisateur{'s' if number_wanted > 1 else ''}.")
    return [get_user() for _ in range(number_wanted)]
