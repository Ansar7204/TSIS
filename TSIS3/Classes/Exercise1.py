import math

class Example:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

instance = Example()
instance.getString()
instance.printString()



class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


shape = Shape()
print(shape.area()) 

square = Square(5)
print(square.area())  




class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(4, 5)
print(rectangle.area())  



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, new_x, new_y):
        self.x = self.x + new_x
        self.y = self.y + new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)


point1 = Point(3, 4)
point2 = Point(6, 8)

point1.show()  
point2.show()  

point1.move(1, 1)
point1.show() 

distance = point1.dist(point2)
print("Distance between point1 and point2:", distance)




class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} accepted. New balance: {self.balance}")
        else:
            print("Deposit amount should be greater than 0.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted. New balance: {self.balance}")
        else:
            print("Insufficient funds. Withdrawal not processed.")


account = BankAccount("Angsar Assilbek", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


prime_numbers = list(filter(lambda x: is_prime(x), numbers))


print(prime_numbers)
