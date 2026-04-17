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
