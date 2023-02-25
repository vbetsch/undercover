import datetime
import argparse
import tarfile
import os
import shutil
import json

BUILD_DIR = '../build'
MAIN_PATH = 'main.py'
MAKE_PATH = 'make.py'

SOURCES_DEST = {
    'src': {
        'type': 'dir',
        'source': 'src',
        'dest': 'src'
    },
    'data': {
        'type': 'dir',
        'source': 'data',
        'dest': 'data'
    },
    'lang': {
        'type': 'file',
        'source': 'lang/%s.json',
        'dest': 'config/%s.json'
    },
    'conf': {
        'type': 'file',
        'source': 'config.json',
        'dest': 'config/config.json'
    },
    'main': {
        'type': 'file',
        'source': 'main.py',
        'dest': 'main.py'
    }
}

default = {
    "PLAYERS": {
        "WHITE_PLAYERS": [],
        "UNDERCOVER_PLAYERS": [],
        "CIVILIAN_PLAYERS": [],
        "ROLE_PLAYERS": {}
    },
    "ROLES": {
        "white": 0,
        "undercover": 0,
        "civilian": 0
    }
}
words = [
    [
        "car",
        "truck"
    ],
    [
        "violin",
        "guitar"
    ],
    [
        "facebook",
        "whatsapp"
    ],
    [
        "youtube",
        "tiktok"
    ]
]
games = []
name_data_dict = {
    "default": default,
    "words": words,
    "games": games
}

NOW = datetime.datetime.now()


def __load(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def __dump(path, data):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def copy_build(build, sources_dest):
    delete_build_if_exist(build)
    if not os.path.exists(build):
        os.mkdir(build)
    for source_dest in sources_dest:
        element = sources_dest[source_dest]
        _type = element['type']
        source = element['source']
        dest = os.path.join(build, element['dest'])
        dir_list = dest.split('/')
        current_dir = build
        for i in range(0, len(dir_list) - 1):
            current_dir = os.path.join(current_dir, dir_list[i])
            if not os.path.exists(current_dir):
                os.mkdir(current_dir)
        if _type == 'dir':
            shutil.copytree(source, dest)
        elif _type == 'file':
            shutil.copyfile(source, dest)
        else:
            raise Exception(f"ERROR: Type {_type} not recognized for {source_dest}")


def modify_conf(build, config):
    config_path = os.path.join(build, config)
    data = __load(config_path)
    data["lang_dir"] = "."
    __dump(config_path, data)


def generate_data(path):
    if not os.path.exists(path):
        os.mkdir(path)
    for name, data in name_data_dict.items():
        __dump(os.path.join(path, f"{name}.json"), data)


def make_tar(filename, source, arc_name):
    with tarfile.open(filename, "w:gz") as tar:
        tar.add(source, arcname=arc_name)


def delete_build_if_exist(build):
    if os.path.exists(build):
        shutil.rmtree(build)


def main():
    parser = argparse.ArgumentParser('%prog ', description='This tool install a pack in shinken')
    parser.add_argument('-l', '--lang', dest='lang', help='Language (required)', required=True)

    opts = parser.parse_args()
    lang = opts.lang

    for source in SOURCES_DEST:
        for prop in SOURCES_DEST[source]:
            if '%s' in SOURCES_DEST[source][prop]:
                if source == 'lang':
                    SOURCES_DEST[source][prop] %= lang

    print("Copying sources...")
    copy_build(BUILD_DIR, SOURCES_DEST)

    print("Generating data files...")
    generate_data(os.path.join(BUILD_DIR, SOURCES_DEST['data']['dest']))

    print("Modify configuration...")
    modify_conf(BUILD_DIR, SOURCES_DEST['conf']['dest'])

    print("Compiling archive...")
    tar_name = f"undercover-{lang}-{NOW.strftime('%Y_%b_%d')}"
    make_tar(f"../{tar_name}.tar.gz", BUILD_DIR, tar_name)

    print("Deleting build folder...")
    delete_build_if_exist(BUILD_DIR)

    print("Done")


if __name__ == '__main__':
    main()
