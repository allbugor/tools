import shutil
import os

# __all__ = ["copy_files_meta", "copy_files", "change_name_if_exists"]

# ! Top-Down func definitions

def copy_files_meta(destination, file_paths):
    _base_copy_files(destination, file_paths)
    return destination


def copy_files(destination, file_paths):
    _base_copy_files(destination, file_paths, with_meta=False)
    return destination


def _base_copy_files(destination, file_paths, with_meta=True):
    for file in file_paths:

        file_name = file.rsplit(os.path.sep, maxsplit=1)[-1]  # Получем имя файла
        dst_file_name = os.path.join(destination, file_name)  # Путь куда копировать с именем файла

        dst_file_name = change_name_if_exists(dst_file_name)

        if with_meta:
            shutil.copy2(file, dst_file_name)
        else:
            shutil.copy(file, dst_file_name)


def change_name_if_exists(dst_name, is_file=True):
        destination, name = dst_name.rsplit(os.path.sep, maxsplit=1)

        # Цикл проверяет если файл/директория уже есть, меняет имя (2), (3), ...
        count = 2
        while os.path.exists(dst_name):
            if is_file:
                new_name = name.replace(".", f"({count}).", count=1)
            else:
                new_name = name + f"({count})"
            dst_name = os.path.join(destination, new_name)
            count +=1

        return dst_name