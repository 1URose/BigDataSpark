import os
import shutil

def copy_folder(src_folder: str, dest_folder: str):
    if not os.path.isdir(src_folder):
        raise FileNotFoundError(f"Исходная папка не найдена: {src_folder}")
    if not os.path.isdir(dest_folder):
        os.makedirs(dest_folder, exist_ok=True)

    folder_name = os.path.basename(src_folder.rstrip(os.sep))

    target_path = os.path.join(dest_folder, folder_name)

    if os.path.exists(target_path):
        shutil.rmtree(target_path)

    # Копируем всю папку целиком
    shutil.copytree(src_folder, target_path)
    print(f"Папка «{src_folder}» успешно скопирована в «{target_path}»")


if __name__ == "__main__":
    source_directory = "исходные данные"
    destination_directory = "notebooks"

    try:
        copy_folder(source_directory, destination_directory)
    except Exception as e:
        print(f"Ошибка при копировании: {e}")
