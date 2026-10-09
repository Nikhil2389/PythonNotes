#super method

class Car:

    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
    
        print("car started...")

    @staticmethod
    def stop():
        print("car started")

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)   #super method used
        self.name=name
        super().start()  #super method used



car1=ToyotaCar("prius","electric")
print(car1.type)                        


