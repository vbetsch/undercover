import json
import os


def __read(path):
    with open(path, 'r') as file:
        return file.readlines()


def __write(path, data):
    with open(path, 'w') as file:
        file.writelines(data)


def __load(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def __dump(path, data):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def __list(filepath, filetype):
    paths = []
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                paths.append(os.path.join(root, file))
    return paths
