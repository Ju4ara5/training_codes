import os

DIRECTORY = r"D:\....\.....\...."  # путь к папке с файлами которык необзодимо переименовать


def rename_files(find_directory):
    for root, dirs, files in os.walk(find_directory):
        for name in files:
            rename_file(root, name)


def rename_file(root, name):
    valid_name = get_valid_name(name)
    old_file = os.path.join(root, name)
    new_file = os.path.join(root, valid_name)
    os.rename(old_file, new_file)


def get_valid_name(name):
    name = name.replace("aaa", "bbb")  # в имени файла "aaa" меняем на "bbb"
    name = name.replace("_w.", "X_")  # в имени файла "_w." меняем на "X_"
    # можно сделать много таких строк

    if not name.startswith("Photo_"):
        name = "Photo_" + name

    return name


if __name__ == '__main__':
    rename_files(DIRECTORY)
