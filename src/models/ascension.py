class Ascension:
    gold: int

    protodisk: int
    protoset: int

    basetier_flower: str
    lowtier_flower: str
    midtier_flower: str
    hightier_flower: str

    gold_item: int

    def __init__(self, gold, protodisk, protoset, basetier_flower, lowtier_flower, midtier_flower, hightier_flower, gold_item):
        self.gold = gold
        self.protodisk = protodisk
        self.protoset = protoset
        self.basetier_flower = basetier_flower
        self.lowtier_flower = lowtier_flower
        self.middtier_flower = midtier_flower
        self.hightier_flower = hightier_flower
        self.gold_item = gold_item

ASCENSIONS = [
    (20, Ascension(1600, 8, 0, 3, 0, 0, 0, 0)),       # 20+
    (40, Ascension(6500, 25, 0, 0, 5, 0, 0, 0)),      # 40+
    (60, Ascension(18000, 0, 24, 0, 0, 5, 0, 0)),     # 60+
    (80, Ascension(100000, 0, 36, 0, 0, 0, 8, 20))    # 80+
]

# ascensione
# - 4 (20+, 40+, 60+, 80+)
#   - gold
#   - protodisk
#   - protoset
#   - flower (variable)
#   - 5* item (variable)
