import json
import os


def __dump(path, data):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    PREFIX = "OK"
    DATA_PATH = 'app\data'
    default = {
        "PLAYERS": {
            "WHITE_PLAYERS"     : [],
            "UNDERCOVER_PLAYERS": [],
            "CIVILIAN_PLAYERS"  : [],
            "ROLE_PLAYERS"      : {}
        },
        "ROLES"  : {
            "white"     : 0,
            "undercover": 0,
            "civilian"  : 0
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
    if not os.path.exists(DATA_PATH):
        os.mkdir(DATA_PATH)
        print(f"{PREFIX} {DATA_PATH} created")
    for name, data in name_data_dict.items():
        file_path = os.path.join(DATA_PATH, f"{name}.json")
        __dump(file_path, data)
        print(f"{PREFIX} {file_path} import")


if __name__ == '__main__':
    main()
    print('Done')
