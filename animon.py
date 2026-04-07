class Animon:
    """Base class for all Animon creatures.

    The getters, calculate_damage, and __str__ are fully implemented.
    You need to implement __eq__ and the three subclasses below.
    """

    def __init__(self, name, power, defense):
        self.name = name
        self.power = power
        self.defense = defense
        self.animon_type = "Normal"

    def get_name(self):
        return self.name

    def get_power(self):
        return self.power

    def get_defense(self):
        return self.defense

    def get_animon_type(self):
        return self.animon_type

    def calculate_damage(self, opponent):
        return max(0, self.power - opponent.get_defense())

    def __eq__(self):
        pass

    def __str__(self):
        return f"[{self.animon_type}] {self.name} (Power: {self.power}, Defense: {self.defense})"


class FireAnimon(Animon):

    def __init__(self):
        pass

    def calculate_damage(self):
        pass


class WaterAnimon(Animon):

    def __init__(self):
        pass

    def calculate_damage(self):
        pass


class GrassAnimon(Animon):

    def __init__(self):
        pass

    def calculate_damage(self):
        pass
