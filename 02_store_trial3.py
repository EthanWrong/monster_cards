"""Component 02: Store cards in catalogue.
Trial 3:
Dict of name-attributes pairs,
 where attributes are stored in a class object of 4 numbers.
Class Creature provides construction of Creature object."""


class Creature:
    def __init__(self, strength, speed, stealth, cunning):
        self.strength = strength
        self.speed = speed
        self.stealth = stealth
        self.cunning = cunning


card_cat = {
    "Stoneling": Creature(7, 1, 25, 15),
    "Vexscream": Creature(1, 6, 21, 19),
    "Dawnmirage": Creature(5, 15, 18, 22),
    "Blazegolem": Creature(15, 20, 23, 6),
    "Websnake": Creature(7, 15, 10, 5),
    "Moldvine": Creature(21, 18, 14, 5),
    "Vortexwing": Creature(19, 13, 19, 2),
    "Rotthing": Creature(16, 7, 4, 12),
    "Froststep": Creature(14, 14, 17, 4),
    "Wispghoul": Creature(17, 19, 3, 2)
}
