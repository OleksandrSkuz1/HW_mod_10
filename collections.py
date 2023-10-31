UserDict = {}  # Словник для зберігання контактів

# Декоратор для обробки помилок введення користувача
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input format."
        except IndexError:
            return "Not enough arguments."
    
    return wrapper

# Функції-обработчики команд
@input_error
def handle_hello():
    return "How can I help you?"

@input_error
def handle_add(contact):
    name, phone = contact.split()
    UserDict[name] = phone
    return "Contact added."

@input_error
def handle_change(contact):
    name, phone = contact.split()
    UserDict[name] = phone
    return "Contact updated."

@input_error
def handle_phone(name):
    phone = UserDict[name]
    return f"Phone number for {name}: {phone}"

@input_error
def handle_show_all():
    if not UserDict:
        return "No contacts found."
    result = "Contacts:\n"
    for name, phone in UserDict.items():
        result += f"{name}: {phone}\n"
    return result

@input_error
def handle_goodbye():
    return "Good bye!"

# Головна функція для взаємодії з користувачем
def main():
    while True:
        command = input("Enter a command: ").lower()
        
        if command == "good bye" or command == "close" or command == "exit":
            print(handle_goodbye())
            break
        elif command == "hello":
            print(handle_hello())
        elif command.startswith("add "):
            print(handle_add(command[4:]))
        elif command.startswith("change "):
            print(handle_change(command[7:]))
        elif command.startswith("phone "):
            print(handle_phone(command[6:]))
        elif command == "show all":
            print(handle_show_all())
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()