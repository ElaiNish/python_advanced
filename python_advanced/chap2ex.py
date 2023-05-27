class Octopus:
    count_animals = 0

    def __init__(self, name="Octavio", age=0):
        self._name = name
        self._age = age
        Octopus.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name

class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        average = (self._red + self._green + self._blue) // 3
        self._red = average
        self._green = average
        self._blue = average

    def print_pixel_info(self):
        color_info = f"Color: ({self._red}, {self._green}, {self._blue})"
        if (self._red == 0 and self._green == 0 and self._blue > 50) or \
                (self._red == 0 and self._green > 50 and self._blue == 0) or \
                (self._red > 50 and self._green == 0 and self._blue == 0):
            color_info += " " + self.get_non_zero_color()
        print(f"X: {self._x}, Y: {self._y}, {color_info}")

    def get_non_zero_color(self):
        if self._red != 0:
            return "Red"
        elif self._green != 0:
            return "Green"
        elif self._blue != 0:
            return "Blue"
        else:
            return ""

class BigThing:
    def __init__(self, var):
        self.var = var

    def size(self):
        if isinstance(self.var, (int, float)):
            return self.var
        else:
            return len(self.var)


class BigCat(BigThing):
    def __init__(self, var, weight):
        super().__init__(var)
        self.weight = weight

    def size(self):
        if self.weight > 20:
            return "Very Fat"
        elif self.weight > 15:
            return "Fat"
        else:
            return "OK"

class Animal:
    zoo_name = "nish_zoo"

    def __init__(self, name, hunger=0):
        self.name = name
        self.hunger = hunger

    def get_name(self):
        return self.name

    def is_hungry(self):
        return self.hunger > 0

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")



class Cat(Animal):
    def talk(self):
        print("meow")
    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    _stink_count = 6

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear Lord!")


class Unicorn(Animal):
    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I'm not your toy...")


class Dragon(Animal):
    _color = "Green"

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")



# Main program
def main():
    # octopus1 = Octopus("liam", 19)
    # octopus2 = Octopus("gilad", 18)
    #
    # octopus1.birthday()
    #
    # print(f"{octopus1.name} is {octopus1.get_age()} years old.")
    # print(f"{octopus2.name} is {octopus2.get_age()} years old.")

    # octopus1 = Octopus("liam")
    # octopus2 = Octopus()
    #
    # print(octopus1.get_name())
    # print(octopus2.get_name())
    #
    # octopus1.set_name("rom")
    # print(octopus1.get_name())
    #
    # print(Octopus.count_animals)

    # p = Pixel(5, 6, 250)
    # p.print_pixel_info()
    # p.set_grayscale()
    # p.print_pixel_info()

    # my_thing = BigThing("balloon")
    # print(my_thing.size())
    #
    # cutie = BigCat("mitzy", 19)
    # print(cutie.size())

    zoo_lst = [
        Dog("Brownie", 10),
        Cat("Zelda", 3),
        Skunk("Stinky"),
        Unicorn("Keith", 7),
        Dragon("Lizzy", 1450),
    ]

    for animal in zoo_lst:
        print(animal.get_name())
        while animal.is_hungry():
            animal.feed()

    for animal in zoo_lst:
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    doggo = Dog("goland", 80)
    kitty = Cat("giorgio", 80)
    stinky_jr = Skunk("liam", 80)
    clair = Unicorn("noa kirel", 80)
    daenerys = Dragon("Syrax", 80)

    zoo_lst.extend([doggo, kitty, stinky_jr, clair, daenerys])

    for animal in zoo_lst:
        print(animal.get_name())
        while animal.is_hungry():
            animal.feed()

    print(Animal.zoo_name)

    return 0


if __name__ == '__main__':
    main()