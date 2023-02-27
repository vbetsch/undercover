from _constants import APP_DIR, SOURCES_DEST, PREFIX, NAME_DATA_DICT
from _core import __dump
import os

data_path = os.path.join(APP_DIR, SOURCES_DEST['data']['source'])


def main():
    if not os.path.exists(data_path):
        os.mkdir(data_path)
        print(f"{PREFIX} {data_path} created")
    for name, data in NAME_DATA_DICT.items():
        file_path = os.path.join(data_path, f"{name}.json")
        __dump(file_path, data)
        print(f"{PREFIX} {file_path} import")


if __name__ == '__main__':
    main()
    print('Done')
