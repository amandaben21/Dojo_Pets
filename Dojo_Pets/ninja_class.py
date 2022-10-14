from pet_class import Pet

class Nija:
      # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food= pet_food

    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self

     # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("Omg!!! You need more pet food")
        
        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()

my_treats = ["Greenies", "Temptations"]
my_pet_food =["Turkey", "Chicken"]


switch = Pet("Switch", "Cat", ["sits", "jumps", "talks"], "meows")
toby = Nija("Toby", "Benitez", switch, my_treats, my_pet_food)

toby.feed()
toby.feed()
toby.feed()
