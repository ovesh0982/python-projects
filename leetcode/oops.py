
class Car:
  def __init__(self,brand,model): 
    self.__brand = brand
    self.model = model

  def get_brand(self):
    return self.__brand + "!"

  def full_car(self): 
    return f"{self.__brand} {self.model}"
  

class ElectricCar(Car):
  def __init__(self,__brand,model,battery_size):
    super().__init__(__brand,model)
    self.battery_size = battery_size

  def full_review(self):
    return f"{self.__brand} {self.battery_size} {self.model}"
  

class Others(ElectricCar):
  def __init__(self, brand, model, battery_size,other):
    super().__init__(brand, model, battery_size)
    self.other = other


my_tesla = ElectricCar("tesla","45","df")
print(my_tesla.full_review())

# other = Others("tesla","ttat","87","mugambo")
# print(other.other)
# my_tesla = ElectricCar("tesla","model s","85khw")
# print(my_tesla.full_review())

# my_car = Car("TOYOTA","COROLLA")
# print(my_car.__brand)
# print(my_car.get_brand())

# print(my_car.full_car())



'''
inheritance
class Sum:
  def __init__(self, a,b,c="result"):
    self.a = a
    self.b = b
    self.c = c
  def sum(self):
    return f"{self.c} = {self.a + self.b}"
  

class Multi(Sum):
  def __init__(self, a, b, c="result"):
    super().__init__(a, b, c)
  def mul(self):
    return f"{self.c} = {self.a * self.b}"


class Min(Sum):
  def __init__(self, a, b, c="result"):
    super().__init__(a, b, c)
  def min(self):
    return f"{self.c} = {self.a - self.b}"


# print(obj.a)
# print(obj.b)
sum = Sum(12,23)
print(sum.a)
print(sum.sum())

mul = Multi(12,22)
print(mul.mul())

min = Min(12,7)
print(min.min())
'''