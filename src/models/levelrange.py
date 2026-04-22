class LevelRange:
    gold: int

    elementary_combat_record: int
    intermediate_combat_record: int
    advanced_combat_record: int

    elementary_cognitive_carrier: int
    advanced_cognitive_carrier: int

    def __init__(
            self, gold: int,
            elementary_combat_record: int, intermediate_combat_record: int, advanced_combat_record: int,
            elementary_cognitive_carrier: int, advanced_cognitive_carrier: int
        ):
        self.gold = gold
        self.elementary_combat_record = elementary_combat_record
        self.intermediate_combat_record = intermediate_combat_record
        self.advanced_combat_record = advanced_combat_record
        self.elementary_cognitive_carrier = elementary_cognitive_carrier
        self.advanced_cognitive_carrier = advanced_cognitive_carrier

LEVEL_RANGES = [
    (1, 20, LevelRange(820, 5, 2, 2, 0, 0)),     # 1-20
    (20, 40, LevelRange(12540, 3, 8, 24, 0, 0)),  # 20-40
    (40, 60, LevelRange(23900, 4, 5, 47, 0, 0)),  # 40-60
    (60, 80, LevelRange(131890, 0, 0, 0, 7, 56)), # 60-80
    (80, 90, LevelRange(252930, 0, 0, 0, 7, 61))  # 80-90
]

# range livello
# - 5 (1-20, 20-40, 40-60, 60-80, 80-90)
#   - gold
#   - libretto lv1
#   - libretto lv2
#   - libretto lv3
#   - libretto lv4
#   - libretto lv5
