# Base class
class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self._power = power  # Encapsulation (protected attribute)
        self.level = level

    def introduce(self):
        print(f"I am {self.name}, my power is {self._power}, and my level is {self.level}!")

    def use_power(self):
        print(f"{self.name} uses {self._power}!")

# Subclass with inheritance and polymorphism
class SpeedHero(Superhero):
    def __init__(self, name, level):
        super().__init__(name, "Super Speed", level)

    def use_power(self):  # Polymorphism
        print(f"{self.name} runs faster than light! ⚡")

# Another subclass
class MindHero(Superhero):
    def __init__(self, name, level):
        super().__init__(name, "Telepathy", level)

    def use_power(self):  # Polymorphism
        print(f"{self.name} reads minds with extreme focus! 🧠")

# Create instances
hero1 = SpeedHero("FlashBolt", 7)
hero2 = MindHero("MindWhisper", 9)

# Call methods
hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()
