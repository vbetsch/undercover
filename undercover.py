from json import load, dump
from random import choice


# --------------------------- JSON ---------------------------
with open('src/data/words.json', 'r') as words_file:
    WORDS = load(words_file)

DATA = {
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

# --------------------------- DATA VARIABLES ---------------------------
PLAYERS = DATA["PLAYERS"]["ROLE_PLAYERS"]
WHITE_PLAYERS = DATA["PLAYERS"]["WHITE_PLAYERS"]
UNDERCOVER_PLAYERS = DATA["PLAYERS"]["UNDERCOVER_PLAYERS"]
CIVILIAN_PLAYERS = DATA["PLAYERS"]["CIVILIAN_PLAYERS"]
ROLES = DATA["ROLES"]

# --------------------------- PLAYERS ---------------------------
sum_players = 5                                 # sum_players = int(input("Players : "))

for index in range(1, sum_players + 1):
    PLAYERS[f"Player{index}"] = None            # PLAYERS[input(f"Name of player ({index}) : ")] = None

# --------------------------- ROLES COUNT ---------------------------
whites = 1                                      # whites = int(input("White : "))
undercovers = 1                                 # undercovers = int(input("Undercover : "))
civilians = 3                                   # civilians = int(input("Civilians : "))

roles = [whites, undercovers, civilians]

if sum_players != sum(roles):
    raise Exception("[ERROR] Sum of players and sum of roles are different")

ROLES["white"] = whites
ROLES["undercover"] = undercovers
ROLES["civilian"] = civilians

# --------------------------- ROLES AFFECTATION ---------------------------
remaining_roles = [
    role_name
    for role_name, role_val in ROLES.items()
    for _ in range(1, role_val + 1)
]

for player in PLAYERS:
    choose_role = choice(remaining_roles)
    remaining_roles.remove(choose_role)
    PLAYERS[player] = choose_role

print(PLAYERS)

for player in PLAYERS:
    match PLAYERS[player]:
        case "white":
            WHITE_PLAYERS.append(player)
        case "undercover":
            UNDERCOVER_PLAYERS.append(player)
        case "civilian":
            CIVILIAN_PLAYERS.append(player)
        case _:
            raise Exception("[ERROR] Someone has nothing role")

# --------------------------- GAME ---------------------------
print(choice(WORDS))

with open('rules.json', 'w', encoding='utf-8') as rules_file:
    dump(DATA, rules_file, ensure_ascii=False, indent=4)
