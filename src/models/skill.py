class Skill:
    gold: int

    protoprism: int
    protohedron: int

    flower: int

    perseverance_mask: int

    gold_item: int

    def __init__(self, gold, protoprism, protohedron, flower, perseverance_mask, gold_item):
        self.gold = gold
        self.protoprism = protoprism
        self.protohedron = protohedron
        self.flower = flower
        self.perseverance_mask = perseverance_mask
        self.gold_item = gold_item
