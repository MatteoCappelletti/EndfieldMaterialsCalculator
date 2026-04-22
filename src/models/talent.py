class Talent:
    gold: int
    protoprism: int
    protohedron: int

    def __init__(self, gold, protoprism, protohedron):
        self.gold = gold
        self.protoprism = protoprism
        self.protohedron = protohedron

COMBAT_TALENTS = [
    Talent(2400, 12, 0),
    Talent(8600, 40, 0),
    Talent(10000, 48, 0),
    Talent(24000, 0, 28)
]

SPACESHIP_TALENTS = [
    Talent(1600, 6, 0),
    Talent(8000, 0, 12),
    Talent(3000, 12, 0),
    Talent(20000, 0, 20)
]

# talent
# - 8
#   - gold
#   - protoprism
#   - protohedron
