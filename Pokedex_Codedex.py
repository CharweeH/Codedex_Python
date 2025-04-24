# Write code below 💖
class Pokemon:
  def __init__(self, entry, name, types, description, is_caught, level, region, height, weight):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught
    self.level = level
    self.region = region
    self.height = height
    self.weight = weight

  def speak(self):
    print(f"{self.name}, {self.name}")

  def display_details(self):
    print(f"Entry Number: {self.entry}")

    print(f"Name: {self.name}")

    if len(self.types) == 1:
      print(f"Type: {self.types[0]}")

    else:
      print(f"Type: {self.types[0]}/{self.types[1]}")

    print(f"Description: {self.description}")

    if self.is_caught:
      print(f"{self.name} has been caught")

    else:
      print(f"{self.name} has't been caught yet")

    print("More Info:")

    print(f"Level: {self.level}")

    print(f"Region: {self.region}")

    print(f"Height: {self.height}m")

    print(f"Weight: {self.weight}kg")

psyduck = Pokemon(54, "Psyduck", ["Water"], "It is constantly wracked by a headache. When the headache turns intense, it begins using mysterious powers.", True, 12, "Kanto", 0.8, 19.6)

psyduck.display_details()

psyduck.speak()