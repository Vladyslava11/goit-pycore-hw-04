from typing import Tuple


def total_salary(path: str) -> Tuple[int, float]:
    """
    Обчислює загальну та середню заробітну плату з файлу.
    
    Файл повинен містити рядки у форматі: ім'я,зарплата
    
    Args:
        path: Шлях до текстового файлу з даними про зарплати
        
    Returns:
        Кортеж із двох чисел: (загальна сума зарплат, середня зарплата)
        Повертає (0, 0) у випадку помилки чи порожнього файлу
        
    Raises:
        FileNotFoundError: Якщо файл не знайдено (перехоплюється)
        ValueError: Якщо дані у файлі не відповідають формату (перехоплюється)
    """
    total: int = 0
    count: int = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                name, salary = line.split(",")
                total += int(salary)
                count += 1

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return 0, 0

    except ValueError:
        print("Помилка: неправильний формат даних у файлі.")
        return 0, 0

    if count == 0:
        return 0, 0

    average: float = total / count
    return total, average


if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
