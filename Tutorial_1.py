
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
    def __init__(self, color, model):
        self._color = color
        self._model = model

    def set_color(self, color):
        self._color = color

    def set_model(self, model):
        self._model = model

    def get_color(self):
        return self._color

    def get_model(self):
        return self._model

# Create a Car object
my_car = Car("Honda", "Blue")

# Access the attributes of the Car object
print("Color of the car: ", my_car.get_color())  # Output: Make of the car:  Honda
print("Model of the car: ", my_car.get_model())
my_car.set_model("Proton")
my_car.set_color("Red")
print("Model of the car: ",my_car.get_model())
print("Color of the car: ",my_car.get_color())


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
