class Ascension:
    gold: int

    protodisk: int
    protoset: int

    flower: int

    gold_item: int

    def __init__(self, gold, protodisk, protoset, flower, gold_item):
        self.gold = gold
        self.protodisk = protodisk
        self.protoset = protoset
        self.flower = flower
        self.gold_item = gold_item

ASCENSIONS = [
    (20, Ascension(1600, 8, 0, 3, 0)),       # 20+
    (40, Ascension(6500, 25, 0, 5, 0)),      # 40+
    (60, Ascension(18000, 0, 24, 5, 0)),     # 60+
    (80, Ascension(100000, 0, 36, 8, 20))    # 80+
]

# ascensione
# - 4 (20+, 40+, 60+, 80+)
#   - gold
#   - protodisk
#   - protoset
#   - flower (variable)
#   - 5* item (variable)
