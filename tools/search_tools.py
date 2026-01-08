import os


# ! Top-Down func definitions

def simple_search(path, query, time_stamp=None, time_now=None):
    matches = []

    for address, dirs, files in os.walk(path):
        for file in files:
            if query not in file:
                continue
            
            full_path = os.path.join(address, file)  # Формируем полный путь к файлу
            if should_add_file(full_path, time_stamp, time_now):
                matches.append(full_path)

    return matches


def should_add_file(full_path, time_stamp, time_now):

    if os.path.islink(full_path):  # Если симлинк пропускаем
        return False
    
    if time_stamp:  # Если есть временной диапазон проверяем
        return time_now - os.path.getctime(full_path) < time_stamp
    
    return True
            