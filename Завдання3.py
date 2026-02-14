import sys
from pathlib import Path

from colorama import Fore, Style, init


def visualize_directory(path: Path, prefix: str = "") -> None:
    """Рекурсивно відображає структуру директорії у вигляді дерева.
    
    Args:
        path: Шлях до директорії для відображення.
        prefix: Префікс для форматування гілок дерева.
        
    Returns:
        None - функція виводить результат напряму в консоль.
    """
    items = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        branch = "└── " if is_last else "├── "
        next_prefix = prefix + ("    " if is_last else "│   ")

        if item.is_dir():
            print(f"{prefix}{branch}{Fore.CYAN}{item.name}")
            visualize_directory(item, next_prefix)
        else:
            print(f"{prefix}{branch}{Fore.GREEN}{item.name}")


def main() -> None:
    """Головна функція програми.
    
    Returns:
        None - функція завершує роботу через sys.exit()
    """
    init(autoreset=True)

    if len(sys.argv) != 2:
        print("Використання: python Завдання3.py /шлях/до/директорії")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(f"Помилка: шлях не існує: {dir_path}")
        sys.exit(1)

    if not dir_path.is_dir():
        print(f"Помилка: це не директорія: {dir_path}")
        sys.exit(1)

    try:
        print(f"{Fore.MAGENTA}{dir_path.name}")
        visualize_directory(dir_path)
    except PermissionError:
        print(f"Помилка: відсутній доступ до деяких файлів: {dir_path}")
    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()