class Monster:
    # Initalizes the Monster
    def __init__(self, name: str, elements: list[str], universe: str, attributes: list[str] = []):
        self.name = name
        self.elements = elements
        self.universe = universe
        self.attributes = attributes