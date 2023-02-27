from constants import NAME_DATA_DICT, SOURCES_DEST, NOW, BUILD_DIR, APP_DIR, DIR, FILE
from core import __list, __read, __write, __load, __dump
import argparse
import tarfile
import os
import shutil


def affect_values(sources_dest, **args):
    for source in sources_dest:
        for prop in sources_dest[source]:
            if '%s' in sources_dest[source][prop]:
                for arg, value in args.items():
                    if source == arg:
                        sources_dest[source][prop] %= value


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
        if _type == DIR:
            shutil.copytree(source, dest)
        elif _type == FILE:
            shutil.copyfile(source, dest)
        else:
            raise Exception(f"ERROR: Type {_type} not recognized for {source_dest}")


def modify_path(build, sources_dest):
    python_files = __list(build, '.py')
    for file in python_files:
        lines = __read(file)
        for i in range(len(lines)):
            if lines[i].startswith('from') and APP_DIR in lines[i]:
                lines[i] = lines[i].replace(f"{APP_DIR}.", "")
            if 'config.json' in lines[i]:
                lines[i] = lines[i].replace(sources_dest['conf']['source'], sources_dest['conf']['dest'])
        __write(file, lines)


def generate_data(path):
    if not os.path.exists(path):
        os.mkdir(path)
    for name, data in NAME_DATA_DICT.items():
        __dump(os.path.join(path, f"{name}.json"), data)


def modify_conf(build, config):
    config_path = os.path.join(build, config)
    data = __load(config_path)
    data["lang_dir"] = "config"
    __dump(config_path, data)


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

    print("Affect values...")
    affect_values(SOURCES_DEST, lang=lang)

    print("Copying sources...")
    copy_build(BUILD_DIR, SOURCES_DEST)

    print("Modify imports...")
    modify_path(BUILD_DIR, SOURCES_DEST)

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
