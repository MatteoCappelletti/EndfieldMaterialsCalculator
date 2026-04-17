import json
from models.character import Character
from models.ascension import Ascension
from models.levelrange import LevelRange
from models.skill import Skill

ASCENSIONS = [
    Ascension(1600, 8, 0, 3, 0),
    Ascension(6500, 25, 0, 5, 0),
    Ascension(18000, 0, 24, 5, 0),
    Ascension(100000, 0, 36, 8, 20)
]

LEVEL_RANGES = [
    LevelRange(820, 5, 2, 2, 0, 0),
    LevelRange(12540, 3, 8, 24, 0, 0),
    LevelRange(23900, 4, 5, 47, 0, 0),
    LevelRange(131890, 0, 0, 0, 7, 56),
    LevelRange(252930, 0, 0, 0, 7, 61)
]

SKILLS = [
    Skill(1000, 6, 0, 1, 0, 0),
    Skill(2700, 12, 0, 2, 0, 0),
    Skill(3200, 16, 0, 1, 0, 0),
    Skill(4200, 21, 0, 1, 0, 0),
    Skill(5400, 27, 0, 2, 0, 0),
    Skill(8200, 0, 6, 1, 0, 0),
    Skill(10500, 0, 8, 1, 0, 0),
    Skill(18000, 0, 15, 2, 0, 0),
    Skill(24000, 0, 15, 3, 1, 6),
    Skill(30000, 0, 24, 6, 2, 16),
    Skill(65000, 0, 50, 12, 3, 36)
]

def characters_import() -> list:

    characters = []
    with open('characters.json', 'r') as file:

        for line in json.load(file):
            try:
                name = line["name"]
                rarity = line["rarity"]
                basetier_flower_name = line["basetier_flower_name"]
                lowtier_flower_name = line["lowtier_flower_name"]
                midtier_flower_name = line["midtier_flower_name"]
                hightier_flower_name = line["hightier_flower_name"]
                basetier_branch_name = line["basetier_branch_name"]
                lowtier_branch_name = line["lowtier_branch_name"]
                midtier_branch_name = line["midtier_branch_name"]
                hightier_branch_name = line["hightier_branch_name"]
                gold_item_name = line["gold_item_name"]

                character = Character(name, rarity,
                                      basetier_flower_name, lowtier_flower_name, midtier_flower_name, hightier_flower_name,
                                      basetier_branch_name, lowtier_branch_name, midtier_branch_name, hightier_branch_name,
                                      gold_item_name)
                characters.append(character)
            except IndexError:
                print(f"Index error: [{line}]")
    return characters

def search_character(characters: list, name: str) -> Character:
    for character in characters:
        if character.name == name:
            return character
    return None

def main():
    characters = characters_import()

    # menu
    # - chiedere il pg
    #   - chiedere cosa si vuole sapere (ascension, skill, talent)
    #     - mostrare i materiali necessari

    # non chiedere all'utente, ma farlo selezionare da una lista di personaggi disponibili
    user_search = input("Nome del pesonaggio: ")

    character = search_character(characters, user_search)
    if character is not None:
        print(character)


if __name__ == "__main__":
    main()

# ascensione
# - 4 (20+, 40+, 60+, 80+)
#   - gold
#   - protodisk
#   - protoset
#   - flower (variable)
#   - 5* item (variable)
# range livello
# - 5 (1-20, 20-40, 40-60, 60-80, 80-90)
#   - gold
#   - libretto lv1
#   - libretto lv2
#   - libretto lv3
#   - libretto lv4
#   - libretto lv5
# skill
# - 12 (1, 2, 3, 4, ... 11, 12)
#   - gold
#   - protoprism
#   - protohedron
#   - flower (variable)
#   - perseverance mark (variable)
#   - 5* item (variable)
# talent
# - 8
#   - gold
#   - protoprism
#   - protohedron
