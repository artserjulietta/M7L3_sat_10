import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  #
    for char in password:
        assert char in valid_characters
def test_password_lenght():
     valid_lenght = 12
     password = generate_password(valid_lenght)
     assert password(len(password)) == valid_lenght 

def test_password_length():
    """Тест, что длина пароля соответствует заданной"""
    for length in [5, 10, 20, 50]:
        password = generate_password(length)
        assert len(password) == length




def test_password_contains_lowercase():
    """Тест, что пароль содержит хотя бы одну строчную букву"""
    password = generate_password(20)
    assert any(c.islower() for c in password)


def test_password_contains_uppercase():
    """Тест, что пароль содержит хотя бы одну заглавную букву"""
    password = generate_password(20)
    assert any(c.isupper() for c in password)


def test_password_contains_digit():
    """Тест, что пароль содержит хотя бы одну цифру"""
    password = generate_password(20)
    assert any(c.isdigit() for c in password)

def test_password_contains_punctuation():
    """Тест, что пароль содержит хотя бы один знак пунктуации"""
    password = generate_password(20)
    assert any(c in string.punctuation for c in password)

def test_password_all_criteria_short_password():
    """Тест, что даже короткий пароль (длина 4) удовлетворяет всем критериям (хотя бы по одному символу каждого типа)"""
    password = generate_password(4)
    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in string.punctuation for c in password)