class Car:
    def __init__(self, model,color):
        self.model=model
        self.color=color

    def show(self):
        print("Name of the model", self.model)
        print("Name of the color", self.color)

audi = Car("Audi a4", "Red")
farrari = Car("Farrari 488", "Blue")

audi.show()
farrari.show()


########################
import datetime

x = datetime.datetime.now()
print(x)
print(x.hour)
print(x.strftime("%A"))
print(x.strftime("%H %M %S"))


