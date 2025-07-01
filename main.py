import sys

tasks = []
name = "Your_name"

# --- Утилиты ---
def separator() -> None:
    print("=" * 20)

def ask_yes_or_no(question: str) -> bool:
    while True:
        answer = input(question)
        if answer.lower() == "да":
            return True
        elif answer.lower() == "нет":
            separator()
            return False
        else:
            print("Пожалуйста, напиши 'да' или 'нет'")

def load_file() -> None:
    try:
        with open("Список задач.txt", "r", encoding="utf-8") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

def save_file() -> None:
    with open("Список задач.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

# --- Основные действия ---

def add_task() -> None:
    while True:
        separator()
        task = input("Введите задачу -> ").strip()
        if not task:
            print("Задача не может быть пустой.")
            continue
        tasks.append(task)
        if not ask_yes_or_no("Задача добавлена. Хотите продолжить? (Да/Нет) -> "):
            break

def show_list() -> None:
    if not tasks:
        print("У вас пока нет задач.")
        return
    separator()
    print("Ваши задачи: ")
    for i, task in enumerate((tasks), start=1):
        print(f"{i}. {task}")
    print(f"Всего задач: {len(tasks)}.")

def delete_task() -> None:
    while True:
        if not tasks:
            print("У вас пока нет задач.")
            return
        separator()
        show_list()
        print(f"Всего задач: {len(tasks)}.")
        success = False
        try:
            number_task = int(input("Введите номер задачи для удаления -> "))
            tasks.pop(number_task-1)
            print("Задача удалена.")
            success = True
        except (ValueError, IndexError):
            print("Некорректный ввод задачи. Попробуйте ещё раз")
            print(f"Введите номер задачи от 1 до {len(tasks)}.")

        if success:
            if not ask_yes_or_no("Хотите удалить ещё? (Да/Нет)"):
                break

def cancel() -> None:
    separator()
    print("Пока!")
    save_file()
    sys.exit()
 
# --- Меню и запуск ---

options = {
    "1": add_task,
    "2": show_list,
    "3": delete_task,
    "4": cancel,
}

def main() -> None:
    while True:
        separator()
        print(f"Привет, {name}! Выберите опцию:\n" \
        "1. Добавить задачу\n" \
        "2. Показать список задач\n" \
        "3. Удалить задачу\n" \
        "4. Завершить работу.")
        user_option = input(">> ")
        action = options.get(user_option)
        if action:
            action()
        else:
            print("Неправильный ввод! Выберите опцию.")
            
if __name__ == "__main__":
    load_file()
    main()
