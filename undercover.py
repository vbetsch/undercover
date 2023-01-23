from json import load, dump
from random import choice

# --------------------------- JSON ---------------------------
words_file = open('words.json', 'r')
WORDS = load(words_file)

DATA = {
    "PLAYERS": {
        "WHITE_PLAYERS": [],
        "UNDERCOVER_PLAYERS": [],
        "CIVIL_PLAYERS": [],
        "ROLE_PLAYERS": {}
    },
    "ROLES": {
        "white": 0,
        "undercover": 0,
        "civil": 0
    }
}

PLAYERS = DATA["PLAYERS"]["ROLE_PLAYERS"]
WHITE_PLAYERS = DATA["PLAYERS"]["WHITE_PLAYERS"]
UNDERCOVER_PLAYERS = DATA["PLAYERS"]["UNDERCOVER_PLAYERS"]
CIVIL_PLAYERS = DATA["PLAYERS"]["CIVIL_PLAYERS"]
ROLES = DATA["ROLES"]

# --------------------------- PLAYERS ---------------------------
sum_players = 5
# sum_players = int(input("Players : "))

for index in range(1, sum_players + 1):
    PLAYERS[f"Player{index}"] = None

# --------------------------- ROLES COUNT ---------------------------
whites = 1
undercovers = 1
civils = 3
# whites = int(input("White : "))
# undercovers = int(input("Undercover : "))
# civils = int(input("Civil : "))

roles = [whites, undercovers, civils]

if sum_players != sum(roles):
    raise Exception("[ERROR] Sum of players and sum of roles are different")


ROLES["white"] = whites
ROLES["undercover"] = undercovers
ROLES["civil"] = civils

# --------------------------- ROLES AFFECTATION ---------------------------
remaining_roles = []
for role in ROLES:
    for index in range(1, ROLES[role] + 1):
        remaining_roles.append(role)

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
        case "civil":
            CIVIL_PLAYERS.append(player)
        case _:
            raise Exception("[ERROR] Someone has nothing role")

# --------------------------- GAME ---------------------------
print(choice(WORDS))

with open('rules.json', 'w', encoding='utf-8') as file:
    dump(DATA, file, ensure_ascii=False, indent=4)
