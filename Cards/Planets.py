class PlanetCard:
    def __init__(self, name, description, price=6, chips=0, mult=0, image=None, isActive=False):
        self.name = name
        self.description = description
        self.price = price
        self.chips = chips
        self.mult = mult
        self.image = image
        self.isActive = isActive

    def __str__(self):
        return f"{self.name}: {self.description}"

    def sellPrice(self):
        return int(self.price * 0.6)

# TODO (TASK 6.1): Implement the Planet Card system for Balatro.
#   Create a dictionary called PLANETS that stores all available PlanetCard objects.
#   Each entry should use the planet's name as the key and a PlanetCard instance as the value.
#   Each PlanetCard must include:
#       - name: the planet's name (e.g., "Mars")
#       - description: the hand it levels up or affects
#       - price: how much it costs to purchase
#       - chips: the chip bonus it provides
#       - mult: the multiplier it applies
#   Example structure:
#       "Gusty Garden": PlanetCard("Gusty Garden", "levels up galaxy", 6, 15, 7)
#   Include all planets up to "Sun" to complete the set.
#   These cards will be used in the shop and gameplay systems to upgrade specific poker hands.


PLANETS = {
    "Mercury": PlanetCard("Mercury", "levels up High Card", 3, 5, 2),
    "Venus": PlanetCard("Venus", "levels up One Pair", 4, 8, 3),
    "Earth": PlanetCard("Earth", "levels up Two Pair", 5, 10, 3),
    "Mars": PlanetCard("Mars", "levels up Three of a Kind", 6, 12, 4),
    "Jupiter": PlanetCard("Jupiter", "levels up Straight", 7, 15, 5),
    "Saturn": PlanetCard("Saturn", "levels up Flush", 8, 18, 5),
    "Uranus": PlanetCard("Uranus", "levels up Full House", 9, 20, 6),
    "Neptune": PlanetCard("Neptune", "levels up Four of a Kind", 10, 25, 7),
    "Pluto": PlanetCard("Pluto", "levels up Straight Flush", 11, 30, 8),
    # The special one → upgrades all hands
    "Sun": PlanetCard("Sun", "levels up everything", 12, 40, 10)

}
