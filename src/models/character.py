class Character:
    name: str
    rarity: int

    basetier_flower_name: str
    lowtier_flower_name: str
    midtier_flower_name: str
    hightier_flower_name: str

    basetier_branch_name: str
    lowtier_branch_name: str
    midtier_branch_name: str
    hightier_branch_name: str

    level_gold_item_name: str
    skill_gold_item_name: str

    def __init__(
            self, name, rarity, 
            basetier_flower_name, lowtier_flower_name, midtier_flower_name, hightier_flower_name,
            basetier_branch_name, lowtier_branch_name, midtier_branch_name, hightier_branch_name,
            level_gold_item_name, skill_gold_item_name
        ):
        self.name = name
        self.rarity = rarity
        self.basetier_flower_name = basetier_flower_name
        self.lowtier_flower_name = lowtier_flower_name
        self.midtier_flower_name = midtier_flower_name
        self.hightier_flower_name = hightier_flower_name
        self.basetier_branch_name = basetier_branch_name
        self.lowtier_branch_name = lowtier_branch_name
        self.midtier_branch_name = midtier_branch_name
        self.hightier_branch_name = hightier_branch_name
        self.level_gold_item_name = level_gold_item_name
        self.skill_gold_item_name = skill_gold_item_name
