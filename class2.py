class Car:
    def __init__ (self,name,brand,capacity):
        self.name = name
        self.brand = brand
        self.capacity = capacity
        self.position = (0,0)
        self.spead = 0
        self.status_engine = False
    

    def cekcarinfo(self):
        print(f"Name Car : {self.name} \nCar brand : {self.brand} \nCar capacity : {self.capacity} \nCar position : {self.position} \nCar status_engine {self.status_engine}")

<<<<<<< HEAD
    def star_engine(self):
        self.status_engine = True
    def stop_engine(self):
        self.status_engine = False

    def accelerate (self,sped)
         self.speed = speed
        if speed > 0:
            self.position = (self.position[0] + speed, self.position[1])
        else:
            self.position = (self.position[0], self.position[1] - speed)
        







=======

carme = Car("Innova","Toyota",40)
carme.cekcarinfo()
>>>>>>> 16e1a23 (Buat Surya)
