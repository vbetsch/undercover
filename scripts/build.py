import datetime
import argparse
import tarfile
import os
import shutil
import json

SRC_PATH = 'src'
DATA_PATH = 'data'
LANG_PATH = 'lang/%s.json'
CONF_PATH = 'config.json'
MAIN_PATH = 'main.py'

BUILD_DIR = '../scripts/build'
MAKE_PATH = 'make.py'

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


def copy_build(build, sources):
    delete_build_if_exist(build)
    if not os.path.exists(build):
        os.mkdir(build)
    for source in sources:
        dest = os.path.join(build, source)
        if os.path.isdir(source):
            shutil.copytree(source, dest)
        elif os.path.isfile(source):
            shutil.copyfile(source, os.path.join(build, os.path.basename(source)))
        else:
            raise Exception("ERROR: File type not recognized")


def modify_conf(build, config):
    data = __load(config)
    data["lang_dir"] = "."
    __dump(os.path.join(build, config), data)


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

    sources = [SRC_PATH, CONF_PATH, MAIN_PATH, LANG_PATH % lang]

    print("Copying sources...")
    copy_build(BUILD_DIR, sources)

    print("Generating data files...")
    generate_data(os.path.join(BUILD_DIR, DATA_PATH))

    print("Modify configuration...")
    modify_conf(BUILD_DIR, CONF_PATH)

    print("Compiling archive...")
    tar_name = f"undercover-{lang}-{NOW.strftime('%Y_%b_%d')}"
    make_tar(f"../{tar_name}.tar.gz", BUILD_DIR, tar_name)

    print("Deleting build folder...")
    delete_build_if_exist(BUILD_DIR)

    print("Done")


if __name__ == '__main__':
    main()
