from crm import User
import pytest
from tinydb import TinyDB, table
from tinydb.storages import MemoryStorage


@pytest.fixture
def setup_db():
    User.db = TinyDB(storage=MemoryStorage)


@pytest.fixture
def user(setup_db):
    u = User(first_name="Juan",
             last_name="Pedro",
             address="1 rue du truc, 91140 Les Ulis",
             phone_number="0660306010")
    u.save()
    return u


def test_full_name(user):
    assert user.full_name == "Juan Pedro"


def test_exists(user):
    assert user.exists() is True


def test_not_exists(user):
    u = User(first_name="Martin",
             last_name="Pedro",
             address="1 rue du truc, 91140 Les Ulis",
             phone_number="0660306010")
    assert u.exists() is False


def test_db_instance(user):
    assert isinstance(user.db_instance, table.Document)
    assert user.db_instance["first_name"] == "Juan"
    assert user.db_instance["last_name"] == "Pedro"
    assert user.db_instance["address"] == "1 rue du truc, 91140 Les Ulis"
    assert user.db_instance["phone_number"] == "0660306010"


def test_not_db_instance(setup_db):
    u = User(first_name="Martin",
             last_name="Pedro",
             address="1 rue du truc, 91140 Les Ulis",
             phone_number="0660306010")
    assert u.db_instance is None


def test__check_phone_number(setup_db):
    user_good = User(first_name="Juan",
                     last_name="Pedro",
                     address="1 rue du truc, 91140 Les Ulis",
                     phone_number="0660306010")

    user_bad = User(first_name="Juan",
                    last_name="Pedro",
                    address="1 rue du truc, 91140 Les Ulis",
                    phone_number="adfd")

    with pytest.raises(ValueError) as err:
        user_bad._check_phone_number()

    assert "invalide" in str(err.value)

    user_good.save(validate_data=True)
    assert user_good.exists() is True


def test__check_names_empty():
    user_bad = User(first_name="",
                    last_name="",
                    address="1 rue du truc, 91140 Les Ulis",
                    phone_number="0660306010")
    with pytest.raises(ValueError) as err:
        user_bad._check_names()

    assert "Le prénom et le nom de famille ne peuvent pas être vides" in str(err.value)


def test__check_names_special_char():
    user_bad = User(first_name="Juan%_-",
                    last_name="Pedro",
                    address="1 rue du truc, 91140 Les Ulis",
                    phone_number="0660306010")
    with pytest.raises(ValueError) as err:
        user_bad._check_names()

    assert "Nom invalide" in str(err.value)


def test_delete(setup_db):
    user_test = User(first_name="Jean",
                     last_name="Pierre",
                     address="1 rue du truc, 91140 Les Ulis",
                     phone_number="0660306010")
    user_test.save()
    first = user_test.delete()
    second = user_test.delete()
    assert len(first) > 0
    assert isinstance(first, list)
    assert len(second) == 0
    assert isinstance(second,list)


def test_save(setup_db):
    user_test = User(first_name="Jean",
                     last_name="Pierre",
                     address="1 rue du truc, 91140 Les Ulis",
                     phone_number="0660306010")
    user_test_duplicate = User(first_name="Jean",
                               last_name="Pierre",
                               address="1 rue du truc, 91140 Les Ulis",
                               phone_number="0660306010")
    first = user_test.save()
    second = user_test_duplicate.save()
    assert isinstance(first, int)
    assert isinstance(second, int)
    assert first > 0
    assert second == -1
