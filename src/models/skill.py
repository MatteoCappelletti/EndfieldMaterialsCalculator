class Skill:
    gold: int

    protoprism: int
    protohedron: int

    flower: int # non è fiore, è branch

    perseverance_mask: int

    gold_item: int

    def __init__(self, gold, protoprism, protohedron, flower, perseverance_mask, gold_item):
        self.gold = gold
        self.protoprism = protoprism
        self.protohedron = protohedron
        self.flower = flower
        self.perseverance_mask = perseverance_mask
        self.gold_item = gold_item

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

# skill
# - 12 (1, 2, 3, 4, ... 11, 12)
#   - gold
#   - protoprism
#   - protohedron
#   - flower (variable)
#   - perseverance mark (variable)
#   - 5* item (variable)
