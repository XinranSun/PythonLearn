class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print("Moving")

    def get_make_model(self):
        print(f"the make is {self.make},\nThe model is {self.model}")


my_car = Vehicle("tes", "Model 1")
my_car.move()
# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
print("----")
your_car = Vehicle("tes", "Model 2")
your_car.get_make_model()

print("------")


class Airplane(Vehicle):
    def __init__(self, make, model, color):
        super().__init__(make, model)
        self.color = color

    def move(self):
        print("flies Moving")


class Truck(Vehicle):
    def move(self):
        print("Truck Moving")


class Apple(Vehicle):
    def move(self):
        print("Apple Moving")


my_airplane = Airplane("fly", "asdas", "red")
my_truck = Truck("truck", "truck")
my_apple = Apple("apple", "asdas")
my_airplane.move()
my_truck.move()
my_apple.move()
print("----------------")

# polymorphism  same input different behave
for v in (my_airplane, my_truck, my_apple):
    print("polymorphism")
    v.get_make_model()