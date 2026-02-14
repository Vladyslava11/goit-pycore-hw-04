def parse_input(user_input: str) -> tuple[str, list[str]]:
    """
    Парсить ввід користувача та розділяє на команду та аргументи.
    
    Рядок розділяється по пробілах. Перше слово - команда,
    решта - аргументи.
    
    Args:
        user_input: Рядок введений користувачем
        
    Returns:
        Кортеж з двох елементів: (команда, список аргументів)
    """
    parts = user_input.strip().split()
    command = parts[0].lower() if parts else ""
    args = parts[1:]
    return command, args


def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Додає новий контакт до словника контактів.
    
    Очікує два аргументи: ім'я та номер телефону.
    
    Args:
        args: Список аргументів [ім'я, телефон]
        contacts: Словник з контактами
        
    Returns:
        Повідомлення про успішне додавання або помилку
        
    Raises:
        ValueError: Якщо передано неправильну кількість аргументів
            (перехоплюється, повертається повідомлення про помилку)
    """
    if len(args) != 2:
        return "Invalid arguments. Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Змінює номер телефону існуючого контакту.
    
    Очікує два аргументи: ім'я та новий номер телефону.
    Якщо контакт не знайдено, повертає повідомлення про помилку.
    
    Args:
        args: Список аргументів [ім'я, телефон]
        contacts: Словник з контактами
        
    Returns:
        Повідомлення про успішне оновлення або помилку
        
    Raises:
        ValueError: Якщо передано неправильну кількість аргументів
            (перехоплюється, повертається повідомлення про помилку)
    """
    if len(args) != 2:
        return "Invalid arguments. Usage: change [name] [phone]"
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """
    Показує номер телефону для вказаного контакту.
    
    Очікує один аргумент: ім'я контакту.
    
    Args:
        args: Список аргументів [ім'я]
        contacts: Словник з контактами
        
    Returns:
        Номер телефону або повідомлення про помилку
        
    Raises:
        IndexError: Якщо не передано ім'я (перехоплюється)
    """
    if len(args) != 1:
        return "Invalid arguments. Usage: phone [name]"
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]


def show_all(contacts: dict[str, str]) -> str:
    """
    Показує всі збережені контакти.
    
    Args:
        contacts: Словник з контактами
        
    Returns:
        Рядок з усіма контактами у форматі "ім'я: телефон",
        або повідомлення якщо контактів немає
    """
    if not contacts:
        return "No contacts saved."
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)


def main() -> None:
    """
    Головна функція бота-асистента.
    
    Запускає інтерактивний цикл обробки команд користувача.
    Підтримує команди: hello, add, change, phone, all, exit
    """
    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
