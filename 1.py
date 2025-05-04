import random
import pathlib
import os

def generate_files(directory, num_files=10, filename_length=8):
    # directory: Путь к папке, где будут созданы файлы
    # num_files: Число файлов для генерации
    # filename_length: Длина имени файла
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    target_path = pathlib.Path(directory)

    if not target_path.exists():
        target_path.mkdir(parents=True)
    generated_files = []
    for _ in range(num_files):
        filename = ''.join(random.choice(characters) for _ in range(filename_length)) + ".txt"
        file_path = target_path / filename
        file_path.touch()
        generated_files.append(file_path)

    for item in generated_files:
        print(item.resolve())

directory = "generated_files"
generate_files(directory)

