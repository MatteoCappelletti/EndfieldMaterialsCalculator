class Skill:
    gold: int

    protoprism: int
    protohedron: int

    basetier_branch: int
    lowtier_branch: int
    midtier_branch: int
    hightier_branch: int

    perseverance_mask: int

    gold_item: int

    def __init__(self, gold, protoprism, protohedron, basetier_branch, lowtier_branch, midtier_branch, hightier_branch, perseverance_mask, gold_item):
        self.gold = gold
        self.protoprism = protoprism
        self.protohedron = protohedron
        self.basetier_branch = basetier_branch
        self.lowtier_branch = lowtier_branch
        self.midtier_branch = midtier_branch
        self.hightier_branch = hightier_branch
        self.perseverance_mask = perseverance_mask
        self.gold_item = gold_item

SKILLS = [
    Skill(1000, 6, 0, 1, 0, 0, 0, 0, 0),
    Skill(2700, 12, 0, 0, 0, 0, 2, 0, 0),
    Skill(3200, 16, 0, 0, 1, 0, 0, 0, 0),
    Skill(4200, 21, 0, 0, 1, 0, 0, 0, 0),
    Skill(5400, 27, 0, 0, 2, 0, 0, 0, 0),
    Skill(8200, 0, 6, 0, 0, 1, 0, 0, 0),
    Skill(10500, 0, 8, 0, 0, 1, 0, 0, 0),
    Skill(18000, 0, 15, 0, 0, 2, 0, 0, 0),
    Skill(24000, 0, 15, 0, 0, 0, 3, 1, 6),
    Skill(30000, 0, 24, 0, 0, 0, 6, 2, 16),
    Skill(65000, 0, 50, 0, 0, 0, 12, 3, 36)
]

# skill
# - 12 (1, 2, 3, 4, ... 11, 12)
#   - gold
#   - protoprism
#   - protohedron
#   - flower (variable)
#   - perseverance mark
#   - 5* item (variable)
