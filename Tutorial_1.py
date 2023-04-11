
#Question 1

def AreaTri():
    base= int(input('Enter Base :'))
    height = int(input('Enter height:'))
    return base * height /2
print(AreaTri())


#Question 2

def num():
    arr = []
    total = 0
    count = 0
    for x in range(10):
        Userinput = int(input('Enter a number '))
        arr.append(Userinput)
        total = total + Userinput
    for x in arr:
        if x >=100:
            count = count +1

    print(count)
    print(total)

num()

class Car:
    def __init__(self, make, model):
        self._make = make
        self._model = model

    def set_make(self, make):
        self._make = make

    def set_model(self, model):
        self._model = model

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

# Create a Car object
my_car = Car("Honda", "blue")

# Access the attributes of the Car object
print("Make of the car: ", my_car.get_make())  # Output: Make of the car:  Honda
print("Model of the car: ", my_car.get_model())


class Employee:
    def __init__(self,name,age,salary):
        self._name = name
        self._age = age
        self._salary = salary

    def increment(self,increment_amount):
        self._salary +=increment_amount

    def higherThan(self,otherEmpolyee):
        if self._salary > otherEmpolyee._salary:
            return True
        else:
            return False


e1 = Employee('John',19,'3000')
e2 = Employee('Gavin',30,'5000')
result = e1.higherThan(e2)
print(result)
