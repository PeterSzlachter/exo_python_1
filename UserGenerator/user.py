import faker
from pprint import pprint

fake = faker.Faker()

def get_user():
    user = f"{fake.first_name()} {fake.last_name()}"
    return user
    
def get_users(number_wanted:int):
    # users = {}
    # for i in range(number_wanted):
    #     users[f"user_{i}"] = get_user()
    # users = []
    # for i in range(number_wanted):
    #     users.append(get_user())
    # return users
    return [get_user() for _ in range(number_wanted)]

pprint(get_users(50))