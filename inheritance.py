#Inheritance

'''when one class(child/derived) derives the properties & method of another class(parent/base).'''
#1.Single Level inheritance

class Car:
    color="black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod  #decorators
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("fortuner")
#car2=ToyotaCar("prius")

car1.start()
car1.stop()
print(car1.color)
print(car1.name)


