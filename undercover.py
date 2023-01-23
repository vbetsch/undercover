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
sum_players = 0
for player in PLAYERS:
    sum_players += 1

sum_roles = 0
for role in ROLES:
    sum_roles += ROLES[role]

if sum_players != sum_roles:
    raise Exception("[ERROR] Sum of players and sum of roles are different")


# Affect roles to players
remaining_roles = []
for role in ROLES:
    for index in range(1, ROLES[role] + 1):
        remaining_roles.append(role)

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
 
