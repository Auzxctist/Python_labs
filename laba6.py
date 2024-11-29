import os
import random
from tkinter import Tk, Button, Label, filedialog, messagebox

created_files = []


def center_window(root, width=400, height=300):
    """Размещает окно по центру экрана."""
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")


def create_random_file(folder, filename, num_count=10, num_range=(1, 10)):
    """Создаёт файл с рандомными числами."""
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, filename)
    with open(file_path, 'w') as file:
        for _ in range(num_count):
            number = random.randint(*num_range)
            file.write(f"{number}\n")
    created_files.append(file_path)


def choose_folder():
    """Открывает диалоговое окно для выбора папки."""
    folder = filedialog.askdirectory(title="Выберите папку для создания файлов")
    return folder


def create_files():
    """Создаёт несколько файлов в выбранной папке."""
    folder = choose_folder()
    if not folder:
        messagebox.showinfo("Отмена", "Папка не выбрана!")
        return

    for i in range(1, 4):
        create_random_file(folder, f"file{i}.txt")
    messagebox.showinfo("Успех", f"Файлы успешно созданы в папке: {folder}")


def delete_files():
    """Удаляет только созданные файлы."""
    deleted = 0
    for file_path in created_files:
        if os.path.exists(file_path):
            os.remove(file_path)
            deleted += 1
    created_files.clear()
    if deleted > 0:
        messagebox.showinfo("Успех", "Созданные файлы успешно удалены!")
    else:
        messagebox.showinfo("Ошибка", "Нет файлов для удаления!")


def calculate_average():
    """Открывает диалоговое окно для выбора файла и вычисляет среднее."""
    filepath = filedialog.askopenfilename(
        title="Выберите файл",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
    )
    if filepath:
        try:
            with open(filepath, 'r') as file:
                numbers = [int(line.strip()) for line in file]
            average = sum(numbers) / len(numbers)
            messagebox.showinfo("Среднее значение", f"Среднее значение: {average:.2f}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось прочитать файл: {e}")
    else:
        messagebox.showinfo("Отмена", "Файл не выбран.")


root = Tk()
root.title("Работа с файлами")


center_window(root, width=400, height=300)


Label(root, text="Работа с файлами", font=("Arial", 14)).pack(pady=10)

Button(root, text="Создать файлы", command=create_files, width=20).pack(pady=5)
Button(root, text="Удалить созданные файлы", command=delete_files, width=20).pack(pady=5)
Button(root, text="Вычислить среднее", command=calculate_average, width=20).pack(pady=5)


root.mainloop()