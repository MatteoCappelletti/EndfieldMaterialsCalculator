import tkinter
from tkinter import ttk
import json
from models.character import Character
from models.ascension import ASCENSIONS
from models.levelrange import LEVEL_RANGES
from models.skill import SKILLS
# from models.talent import COMBAT_TALENTS, SPACESHIP_TALENTS

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

                character = Character(
                    name, rarity,
                    basetier_flower_name, lowtier_flower_name, midtier_flower_name, hightier_flower_name,
                    basetier_branch_name, lowtier_branch_name, midtier_branch_name, hightier_branch_name,
                    gold_item_name
                )
                characters.append(character)
            except IndexError:
                print(f"Index error: [{line}]")
    return characters

def search_character(characters: list, name: str) -> Character:
    for character in characters:
        if character.name == name:
            return character
    return None

def app():
    CHARACTER_STARTING_ROW = 0  # 1 riga richiesta
    LEVEL_STARTING_ROW = 1      # 1
    SKILLS_STARTING_ROW = 2     # 4
    CALC_BUTTON_ROW = 6         # 1
    RESULTS_STARTING_ROW = 7    # N calcolato

    window = tkinter.Tk()
    window.title("Endfield Mats Calculator")
    window.geometry("1600x1000")
    window.columnconfigure(0, weight=1)

    # all mats variables

    gold_from_level = 0
    gold_from_skill = 0
    protodisk = 0
    protoset = 0
    flower = 0
    gold_item = 0
    elementary_combat_record = 0
    intermediate_combat_record = 0
    advanced_combat_record = 0
    elementary_cognitive_carrier = 0
    advanced_cognitive_carrier = 0
    protoprism = 0
    protohedron = 0
    perseverance_mask = 0

    def reset_mats():
        nonlocal gold_from_level
        nonlocal gold_from_skill
        nonlocal protodisk
        nonlocal protoset
        nonlocal flower
        nonlocal gold_item
        nonlocal elementary_combat_record
        nonlocal intermediate_combat_record
        nonlocal advanced_combat_record
        nonlocal elementary_cognitive_carrier
        nonlocal advanced_cognitive_carrier
        nonlocal protoprism
        nonlocal protohedron
        nonlocal perseverance_mask

        gold_from_level = 0
        gold_from_skill = 0
        protodisk = 0
        protoset = 0
        flower = 0
        gold_item = 0
        elementary_combat_record = 0
        intermediate_combat_record = 0
        advanced_combat_record = 0
        elementary_cognitive_carrier = 0
        advanced_cognitive_carrier = 0
        protoprism = 0
        protohedron = 0
        perseverance_mask = 0

    # mats labels

    mats_labels = []

    def forget_mats_labels():
        nonlocal mats_labels

        for label in mats_labels:
            label.grid_forget()
        mats_labels = []

    def show_mats_label(row: int, value: int, name: str):
        label = tkinter.Label(
            window, text=f"{value} {name}")
        label.grid(row=row, column=0, padx=100, pady=10)
        return label

    def reload_mats_labels():
        forget_mats_labels()

        character = search_character(characters_import(), character_combobox.get())

        row = RESULTS_STARTING_ROW

        gold = gold_from_level + gold_from_skill
        if gold != 0:
            mats_labels.append(show_mats_label(row, gold, "gold"))

        if protodisk != 0:
            row += 1
            mats_labels.append(show_mats_label(row, protodisk, "protodisk"))

        if protoset != 0:
            row += 1
            mats_labels.append(show_mats_label(row, protoset, "protoset"))

        if flower != 0:
            row += 1
            mats_labels.append(show_mats_label(row, flower, "flower"))

        if gold_item != 0:
            row += 1
            mats_labels.append(show_mats_label(row, gold_item, character.gold_item_name))

        if elementary_combat_record != 0:
            row += 1
            mats_labels.append(show_mats_label(row, elementary_combat_record, "elementary_combat_record"))

        if intermediate_combat_record != 0:
            row += 1
            mats_labels.append(show_mats_label(
                row, intermediate_combat_record, "intermediate_combat_record"))

        if advanced_combat_record != 0:
            row += 1
            mats_labels.append(show_mats_label(
                row, advanced_combat_record, "advanced_combat_record"))

        if elementary_cognitive_carrier != 0:
            row += 1
            mats_labels.append(show_mats_label(
                row, elementary_cognitive_carrier, "elementary_cognitive_carrier"))

        if advanced_cognitive_carrier != 0:
            row += 1
            mats_labels.append(show_mats_label(
                row, advanced_cognitive_carrier, "advanced_cognitive_carrier"))

        if protoprism != 0:
            row += 1
            mats_labels.append(show_mats_label(
                row, protoprism, "protoprism"))

        if protohedron != 0:
            row += 1
            mats_labels.append(show_mats_label(
                row, protohedron, "protohedron"))

        if perseverance_mask != 0:
            row += 1
            mats_labels.append(show_mats_label(
                row, perseverance_mask, "perseverance_mask"))

    # select a character

    character_names = [character.name for character in characters_import()]

    character_label = tkinter.Label(window, text="Seleziona il tuo personaggio:")
    character_label.grid(row=CHARACTER_STARTING_ROW, column=0, padx=10, pady=10)

    character_combobox = ttk.Combobox(window, values=character_names, state="readonly")
    character_combobox.grid(row=CHARACTER_STARTING_ROW, column=1, padx=10, pady=10)
    character_combobox.current(0)

    # character levels

    level_options = ["1", "20", "20+", "40", "40+", "60", "60+", "80", "80+", "90"]

    actual_level_label = tkinter.Label(window, text="Seleziona il tuo livello attuale e finale:")
    actual_level_label.grid(row=LEVEL_STARTING_ROW, column=0, padx=10, pady=10)

    actual_level_combobox = ttk.Combobox(window, values=level_options, state="readonly")
    actual_level_combobox.grid(row=LEVEL_STARTING_ROW, column=1, padx=10, pady=10)
    actual_level_combobox.current(0)

    final_level_label = tkinter.Label(window, text="->")
    final_level_label.grid(row=LEVEL_STARTING_ROW, column=2, padx=10, pady=10)

    final_level_combobox = ttk.Combobox(window, values=level_options, state="readonly")
    final_level_combobox.grid(row=LEVEL_STARTING_ROW, column=3, padx=10, pady=10)
    final_level_combobox.current(len(level_options) - 1)

    def levels_mats_calc():

        actual_level_scelta = actual_level_combobox.get()
        final_level_scelta = final_level_combobox.get()

        start_level = int(actual_level_scelta.replace("+", ""))
        final_level = int(final_level_scelta.replace("+", ""))

        nonlocal gold_from_level
        nonlocal protodisk
        nonlocal protoset
        nonlocal flower # da mettere _from_level
        nonlocal gold_item # da mettere _from_level
        nonlocal elementary_combat_record
        nonlocal intermediate_combat_record
        nonlocal advanced_combat_record
        nonlocal elementary_cognitive_carrier
        nonlocal advanced_cognitive_carrier

        if start_level == final_level and "+" not in actual_level_scelta and "+" in final_level_scelta:
            for ascension_level, ascension_mats in ASCENSIONS:
                if ascension_level == start_level:
                    gold_from_level += ascension_mats.gold
                    protodisk += ascension_mats.protodisk
                    protoset += ascension_mats.protoset
                    flower += ascension_mats.flower
                    gold_item += ascension_mats.gold_item
                    break
        else:
            for start_range_level, max_range_level, mats in LEVEL_RANGES:
                # ho aggiunto i global var perché:
                # UnboundLocalError: cannot access local variable 'gold' where it is not associated with a value

                if start_level <= start_range_level and final_level >= max_range_level:
                    # aggiungi mats range

                    gold_from_level += mats.gold
                    elementary_combat_record += mats.elementary_combat_record
                    intermediate_combat_record += mats.intermediate_combat_record
                    advanced_combat_record += mats.advanced_combat_record
                    elementary_cognitive_carrier += mats.elementary_cognitive_carrier
                    advanced_cognitive_carrier += mats.advanced_cognitive_carrier

                    if start_level != 1 and start_level == start_range_level and "+" not in actual_level_scelta:
                        # aggiungi mats ascesion di start_range_level

                        for ascension_level, ascension_mats in ASCENSIONS:
                            if ascension_level == start_range_level:
                                gold_from_level += ascension_mats.gold
                                protodisk += ascension_mats.protodisk
                                protoset += ascension_mats.protoset
                                flower += ascension_mats.flower
                                gold_item += ascension_mats.gold_item
                                break

                    if final_level == max_range_level and "+" in final_level_scelta:
                        # aggiungi mats ascension di max_range_level

                        for ascension_level, ascension_mats in ASCENSIONS:
                            if ascension_level == max_range_level:
                                gold_from_level += ascension_mats.gold
                                protodisk += ascension_mats.protodisk
                                protoset += ascension_mats.protoset
                                flower += ascension_mats.flower
                                gold_item += ascension_mats.gold_item
                                break

                    if start_level < start_range_level:
                        # aggiungi mats ascension di start_range_vel

                        for ascension_level, ascension_mats in ASCENSIONS:
                            if ascension_level == start_range_level:
                                gold_from_level += ascension_mats.gold
                                protodisk += ascension_mats.protodisk
                                protoset += ascension_mats.protoset
                                flower += ascension_mats.flower
                                gold_item += ascension_mats.gold_item
                                break

    # skills

    skill_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # si potrebbe fare un generator (non so se è utile)

    initial_skill_row = SKILLS_STARTING_ROW
    actual_skill_labels = []
    final_skill_labels = []
    skill_comboboxes = []

    # inizializzazione skill labels e comboboxes
    for i in range(4):
        actual_skill_label = tkinter.Label(window, text=f"Skill {i + 1}:")
        actual_skill_label.grid(row=(initial_skill_row + i), column=0, padx=10, pady=10)
        actual_skill_labels.append(actual_skill_label)

        actual_skill_combobox = ttk.Combobox(window, values=skill_option, state="readonly")
        actual_skill_combobox.grid(row=(initial_skill_row + i), column=1, padx= 10, pady=10)
        actual_skill_combobox.current(0)

        final_skill_label = tkinter.Label(window, text="->")
        final_skill_label.grid(row=(initial_skill_row + i), column=2, padx=10, pady=10)
        final_skill_labels.append(final_skill_label)

        final_skill_combobox = ttk.Combobox(window, values=skill_option, state="readonly")
        final_skill_combobox.grid(row=(initial_skill_row + i), column=3, padx= 10, pady=10)
        final_skill_combobox.current(len(skill_option) - 1)

        skill_comboboxes.append((actual_skill_combobox, final_skill_combobox))

    def skills_mats_calc():
        nonlocal gold_from_skill
        nonlocal protoprism
        nonlocal protohedron
        nonlocal flower # da mettere _from_skill
        nonlocal perseverance_mask
        nonlocal gold_item # da mettere _from_skill

        for start_skill_combobox, final_skill_combobox in skill_comboboxes:
            start_skill = start_skill_combobox.get()
            final_skill = final_skill_combobox.get()

            for i in range(int(start_skill) - 1, int(final_skill) - 1):
                gold_from_skill += SKILLS[i].gold
                protoprism += SKILLS[i].protoprism
                protohedron += SKILLS[i].protohedron
                flower += SKILLS[i].flower
                perseverance_mask += SKILLS[i].perseverance_mask
                gold_item += SKILLS[i].gold_item

    # show on screen

    def do_all_calculations():
        reset_mats()

        levels_mats_calc()
        skills_mats_calc()

        reload_mats_labels()

    level_button = ttk.Button(window, text="Calcola", command=do_all_calculations)
    level_button.grid(row=CALC_BUTTON_ROW, column=0, padx=10, pady=10)

    reload_mats_labels()

    window.mainloop()

if __name__ == "__main__":
    app()
