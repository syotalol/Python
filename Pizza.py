class Topping:
    def __init__(self, topping_name):
        self.topping_name = topping_name

    def get_topping(self):
        print ("Уou choose the topping: " + self.topping_name)


class Sauce:
    def __init__(self, sauce_name):
        self.sauce_name = sauce_name

    def get_sauce(self):
        print ("You choose the sauce: " + self.sauce_name)


class Pizza(Topping, Sauce):
    def __init__(self, topping_name, sauce_name, pizza_name, dough, diameter):
        self.topping_name = topping_name
        self.sauce_name = sauce_name
        self.pizza_name = pizza_name
        self.dough = dough
        self.diameter = diameter

    def get_pizza(self):
        print ("Your order: pizza - {0} (dough - {1}, diameter - {2}).".format(self.pizza_name, self.dough, self.diameter))


pizza = Pizza("anchovies", "pink", "4cheese", "thin", "35")

pizza.get_pizza()
pizza.get_topping()
pizza.get_sauce()

