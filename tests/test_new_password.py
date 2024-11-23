import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_password_length():
    """Тест, что длина пароля соответствует заданной"""
    for length in [5, 10, 20, 50]:
        password = generate_password(length)
        assert len(password) == length

def test_password_uniqueness():
    """Тест, что два сгенерированных подряд пароля различаются"""
    password1 = generate_password(20)  # Используем достаточную длину, чтобы снизить вероятность совпадения
    password2 = generate_password(20)
    assert password1 != password2


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
