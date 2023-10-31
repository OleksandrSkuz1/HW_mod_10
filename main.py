from collections import UserDict

# Створюємо батьківський клас у ньому реалізується логіка загальна для всіх полів
class Field:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу

class Phone(Field):
    # реалізація класу

class Record:
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones = []

    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу