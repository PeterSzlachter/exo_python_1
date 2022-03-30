from faker import Faker

fake = Faker(locale="fr_FR")

print(fake.name())
print(fake.unique.name())
print(fake.text())
print(fake.address())

numbers = [fake.unique.random_int() for _ in range(10)]
assert len(numbers) == len(set(numbers)) #assert teste la condition
print(numbers)

# print([fake.job() for _ in range(10)])
# print([fake.file_path() for _ in range(10)])
# print([fake.credit_card_number() + " " + fake.credit_card_expire() + " " + fake.credit_card_security_code() for _ in range(10)])

# print([fake.rgb_color() for _ in range(10)])
# print([fake.hex_color() for _ in range(10)])
# print([fake.numerify(text="%%%-%-%%%%-%%%%-%%%%-%%%-##") for _ in range(5)])
print([fake.bothify(text="Product Number : ????-#######") for _ in range(5)])