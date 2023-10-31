from collections import UserDict

class Field:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    ...

class Phone(Field):
    def __init__(self, value) -> None:
        if not self.is_valid_phone(value):
            raise ValueError("Invalid phone number format")
        super().__init__(value)

    @staticmethod
    def is_valid_phone(value):
        return len(value) == 10 and value.isdigit()

class Record:
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: int):
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone: int):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)

    def edit_phone(self, old_phone: int, new_phone: int):
        found = False  # Додана змінна для відстеження, чи знайдено номер
        if Phone.is_valid_phone(new_phone):
            for p in self.phones:
                if p.value == old_phone:
                    p.value = new_phone
                    found = True  # Позначити, що номер знайдено
            if not found:
                raise ValueError(f"Phone number '{old_phone}' not found")
        else:
            raise ValueError("Invalid phone number format")


    def find_phone(self, phone: int):
        for p in self.phones:
            if p.value == phone:
                return p  


    def __str__(self):
        phones_str = "; ".join(str(p) for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name: list):
        if name in self.data:
            return self.data[name]

    def delete(self, name: list):
        if name in self.data:
            del self.data[name]

# Приклад використання:
book = AddressBook()
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name.value}: {found_phone}")

book.delete("Jane")
