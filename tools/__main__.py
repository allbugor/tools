import os
import sys
import time

try:
    from . import simple_search
    from . import zip_archive
    from . import copy_files_meta, change_name_if_exists
except:
    from search_tools import simple_search
    from backup.archive_tools import zip_archive
    from backup.copy_tools import *
    
# ! Bottom-Up func definitions

def run_task(task, matches):
    if task == "0":
        return
    
    cwd = os.getcwd()
    path_for_copy = os.path.join(cwd, "copied")
    path_for_copy = change_name_if_exists(path_for_copy, is_file=False)
    os.mkdir(path_for_copy)
    
    if task == "1":
        path = copy_files_meta(path_for_copy, matches)
        print(f"Скопировано в {path}")
    elif task == "2":
        archive_name = "backup-" + time.strftime("%Y-%m-%d_%H-%M-%S")
        dst = os.path.join(cwd, archive_name)
        target_dir = copy_files_meta(path_for_copy, matches)
        path = zip_archive(dst, target_dir, delete_target=True)
        print(f"Архив: {path}")


def get_task():
    commands = ("0", "1", "2")
    while True:
        command = input(f"Копировать - 1, Архивировать - 2, Отмена - 0\n>> ")
        if command in commands:
            return command
        print(f"Читаем внимательно, варианты: {commands}")


def get_search_params():
    start_path = input("Введите путь (пустой ввод - текущий cwd)\n>> ") or os.getcwd()

    if not os.path.isdir(start_path):
        print(f"Ошибка: {start_path} не является директорией или не существует.")
        sys.exit(1)
    
    query = input("Что ищем?\n>> ")
    prompt = "Сколько часов назад был создан файл, или пустой ввод:\n"">> "
    time_stamp = int(input(prompt) or 0) * 3600
    time_now = time.time()

    return start_path, query, time_stamp, time_now


def main():
    params = get_search_params()
    matches = simple_search(*params)
    print(f"Найдено {len(matches)} файлов.")

    if not matches:
        return
    
    task = get_task()
    run_task(task, matches)
    

if __name__ == "__main__":
    main()

