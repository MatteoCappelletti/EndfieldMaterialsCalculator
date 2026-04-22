import tkinter
from tkinter import ttk
import json
from models.character import Character
from models.ascension import ASCENSIONS
from models.levelrange import LEVEL_RANGES
from models.skill import SKILLS
from models.talent import COMBAT_TALENTS, SPACESHIP_TALENTS


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
        richiesta = input("Vuoi aumentare il livello? ")
        if richiesta == "y":
            pass
        richiesta = input("Vuoi aumentare le skill? ")
        if richiesta == "y":
            pass
        richiesta = input("Vuoi aumentare i talenti di combattimento? ")
        if richiesta == "y":
            pass
        richiesta = input("Vuoi aumentare i talenti dell'astronave? ")
        if richiesta == "y":
            pass

def app():
    window = tkinter.Tk()
    window.title("Endfield Mats Calculator")
    window.geometry("1900x500")
    window.columnconfigure(0, weight=1)

    # mats to show on screen

    gold = 0
    protodisk = 0
    protoset = 0
    flower = 0
    gold_item = 0
    elementary_combat_record = 0
    intermediate_combat_record = 0
    advanced_combat_record = 0
    elementary_cognitive_carrier = 0
    advanced_cognitive_carrier = 0

    def reset_mats():
        nonlocal gold
        nonlocal protodisk
        nonlocal protoset
        nonlocal flower
        nonlocal gold_item
        nonlocal elementary_combat_record
        nonlocal intermediate_combat_record
        nonlocal advanced_combat_record
        nonlocal elementary_cognitive_carrier
        nonlocal advanced_cognitive_carrier

        gold = 0
        protodisk = 0
        protoset = 0
        flower = 0
        gold_item = 0
        elementary_combat_record = 0
        intermediate_combat_record = 0
        advanced_combat_record = 0
        elementary_cognitive_carrier = 0
        advanced_cognitive_carrier = 0

    # character levels

    level_options = ["1", "20", "20+", "40", "40+", "60", "60+", "80", "80+", "90"]

    actual_level_label = tkinter.Label(window, text="Seleziona il tuo livello attuale e finale:")
    actual_level_label.grid(row=0, column=0, padx=10, pady=10)

    actual_level_combobox = ttk.Combobox(window, values=level_options, state="readonly")
    actual_level_combobox.grid(row=0, column=1, padx=10, pady=10)
    actual_level_combobox.current(0)

    final_level_label = tkinter.Label(window, text="->")
    final_level_label.grid(row=0, column=2, padx=10, pady=10)

    final_level_combobox = ttk.Combobox(window, values=level_options, state="readonly")
    final_level_combobox.grid(row=0, column=3, padx=10, pady=10)
    final_level_combobox.current(len(level_options) - 1)

    def level_combobox(event):
        reset_mats()

        actual_level_scelta = actual_level_combobox.get()
        final_level_scelta = final_level_combobox.get()

        start_level = int(actual_level_scelta.replace("+", ""))
        final_level = int(final_level_scelta.replace("+", ""))

        for start_range_level, max_range_level, mats in LEVEL_RANGES:
            # ho aggiunto i global var perché:
            # UnboundLocalError: cannot access local variable 'gold' where it is not associated with a value

            if start_level >= start_range_level and final_level <= max_range_level:
                # aggiungi mats range

                nonlocal gold
                nonlocal protodisk
                nonlocal protoset
                nonlocal flower
                nonlocal gold_item
                nonlocal elementary_combat_record
                nonlocal intermediate_combat_record
                nonlocal advanced_combat_record
                nonlocal elementary_cognitive_carrier
                nonlocal advanced_cognitive_carrier

                gold += mats.gold
                elementary_combat_record += mats.elementary_combat_record
                intermediate_combat_record += mats.intermediate_combat_record
                advanced_combat_record += mats.advanced_combat_record
                elementary_cognitive_carrier += mats.elementary_cognitive_carrier
                advanced_cognitive_carrier += mats.advanced_cognitive_carrier

                if start_level == start_range_level and "+" not in actual_level_scelta:
                    # aggiungi mats ascesion di start_range_level

                    for ascension_level, ascension_mats in ASCENSIONS:
                        if ascension_level == start_range_level:
                            gold += ascension_mats.gold
                            protodisk += ascension_mats.protodisk
                            protoset += ascension_mats.protoset
                            flower += ascension_mats.flower
                            gold_item += ascension_mats.gold_item
                            break

                elif final_level == max_range_level and "+" in final_level_scelta:
                    # aggiungi mats ascension di max_range_level

                    for ascension_level, ascension_mats in ASCENSIONS:
                        if ascension_level == max_range_level:
                            gold += ascension_mats.gold
                            protodisk += ascension_mats.protodisk
                            protoset += ascension_mats.protoset
                            flower += ascension_mats.flower
                            gold_item += ascension_mats.gold_item
                            break

                elif start_level > start_range_level and final_level < max_range_level:
                    # aggiungi mats ascension di start_range_vel

                    for ascension_level, ascension_mats in ASCENSIONS:
                        if ascension_level == start_range_level:
                            gold += ascension_mats.gold
                            protodisk += ascension_mats.protodisk
                            protoset += ascension_mats.protoset
                            flower += ascension_mats.flower
                            gold_item += ascension_mats.gold_item
                            break
        reload_mats()

    actual_level_combobox.bind("<<ComboboxSelected>>", level_combobox)
    final_level_combobox.bind("<<ComboboxSelected>>", level_combobox)

    # skills

    # talents

    # show on screen

    def reload_mats():
        initial_show_row = 1
        if gold != 0:
            label_gold = tkinter.Label(
                window, text=f"{gold} gold")
            label_gold.grid(row=initial_show_row, column=0, padx=100, pady=10)

        if protodisk != 0:
            initial_show_row += 1
            label_protodisk = tkinter.Label(
                window, text=f"{protodisk} protodisk")
            label_protodisk.grid(row=initial_show_row, column=0, padx=100, pady=10)

        if protoset != 0:
            initial_show_row += 1
            label_protoset = tkinter.Label(
                window, text=f"{protoset} protoset")
            label_protoset.grid(row=initial_show_row, column=0, padx=100, pady=10)

        if flower != 0:
            initial_show_row += 1
            label_flower = tkinter.Label(
                window, text=f"{flower} flower")
            label_flower.grid(row=initial_show_row, column=0, padx=100, pady=10)

        if gold_item != 0:
            initial_show_row += 1
            label_gold_item = tkinter.Label(
                window, text=f"{gold_item} gold item")
            label_gold_item.grid(row=initial_show_row, column=0, padx=100, pady=10)

        if elementary_combat_record != 0:
            initial_show_row += 1
            label_elementary_combat_record = tkinter.Label(
                window, text=f"{elementary_combat_record} elementary combat record")
            label_elementary_combat_record.grid(row=initial_show_row, column=0, padx=100, pady=10)

        if intermediate_combat_record != 0:
            initial_show_row += 1
            label_intermediate_combat_record = tkinter.Label(
                window, text=f"{intermediate_combat_record} gintermediate combat recordold")
            label_intermediate_combat_record.grid(row=initial_show_row, column=0, padx=100, pady=10)

        if advanced_combat_record != 0:
            initial_show_row += 1
            label_advanced_combat_record = tkinter.Label(
                window, text=f"{advanced_combat_record} advanced combat record")
            label_advanced_combat_record.grid(row=initial_show_row, column=0, padx=100, pady=10)

        if elementary_cognitive_carrier != 0:
            initial_show_row += 1
            label_elementary_cognitive_carrier = tkinter.Label(
                window, text=f"{elementary_cognitive_carrier} elementary cognitive carrier")
            label_elementary_cognitive_carrier.grid(row=initial_show_row, column=0, padx=100, pady=10)

        if advanced_cognitive_carrier != 0:
            initial_show_row += 1
            label_advanced_cognitive_carrier = tkinter.Label(
                window, text=f"{advanced_cognitive_carrier} advanced cognitive carrier")
            label_advanced_cognitive_carrier.grid(row=initial_show_row, column=0, padx=100, pady=10)

    reload_mats()

    window.mainloop()

if __name__ == "__main__":
    # main()
    app()
