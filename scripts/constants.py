import datetime


# DATETIME
NOW = datetime.datetime.now()

# CLI
PREFIX = "OK"

# FILE TYPES
DIR = 'dir'
FILE = 'file'

# PATH
APP_DIR = 'app'
BUILD_DIR = '../build'
MAKE_PATH = 'make.py'
SOURCES_DEST = {
    'src': {
        'type': DIR,
        'source': 'src',
        'dest': 'src'
    },
    'data': {
        'type': DIR,
        'source': 'data',
        'dest': 'data'
    },
    'lang': {
        'type': FILE,
        'source': 'lang/%s.json',
        'dest': 'config/%s.json'
    },
    'conf': {
        'type': FILE,
        'source': 'config.json',
        'dest': 'config/config.json'
    },
    'main': {
        'type': FILE,
        'source': 'main.py',
        'dest': 'main.py'
    }
}

# DATA
DEFAULT = {
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
WORDS = [
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
GAMES = []
NAME_DATA_DICT = {
    "default": DEFAULT,
    "words": WORDS,
    "games": GAMES
}
