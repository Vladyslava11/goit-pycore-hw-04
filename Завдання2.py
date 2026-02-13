def get_cats_info(path: str) -> list[dict[str, str | int]]:
    """
    Читає файл з інформацією про котів та повертає список словників.
    
    Файл повин містити рядки у форматі: id,name,age
    Кожен рядок конвертується у словник з ключами 'id', 'name', 'age'.
    
    Args:
        path: Шлях до текстового файлу з даними про котів
        
    Returns:
        Список словників з інформацією про котів. 
        Порожній список повертається у випадку помилки чи порожнього файлу.
        
    Raises:
        FileNotFoundError: Якщо файл не знайдено (перехоплюється, 
            повертається порожній список)
        ValueError: Якщо дані у файлі не відповідають формату 
            (перехоплюється, повертається порожній список)
    """
    cats: list[dict[str, str | int]] = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                cat_id, name, age = line.split(",")

                cat: dict[str, str | int] = {
                    "id": cat_id,
                    "name": name,
                    "age": int(age),
                }

                cats.append(cat)

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return []

    except ValueError:
        print("Помилка: неправильний формат даних у файлі.")
        return []

    return cats


if __name__ == "__main__":
    cats_info = get_cats_info("cats.txt")
    print(cats_info)