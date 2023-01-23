from json import load
from random import choice


# JSON
rules_file = open('rules.json', 'r')
RULES = load(rules_file)


# Rules
PLAYERS = RULES["PLAYERS"]
ROLES = RULES["ROLES"]
WORDS = RULES["WORDS"]


# Test rules
sum_players = len(PLAYERS.keys())
sum_roles = sum(ROLES.values())

if sum_players != sum_roles:
    raise Exception("[ERROR] Sum of players and sum of roles are different")


# Affect roles to players
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

WHITE_PLAYERS = []
UNDERCOVER_PLAYERS = []
CIVIL_PLAYERS = []

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


print(choice(WORDS))
