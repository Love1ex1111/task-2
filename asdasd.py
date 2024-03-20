from math import sqrt
class Point:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def calculate_distance(self, coord_x_1, coord_y_1):
        return sqrt((self.coord_x - coord_x_1) ** 2 + (self.coord_y - coord_y_1) ** 2 )

point_one = Point(coord_x=2, coord_y=3)
print(point_one.calculate_distance(coord_x_1=2, coord_y_1=5))




class Bank_akkaynt:
    def __init__(self):
        self.balance = 0

    def deposit(self, money):
        self.balance += money

    def winthdraw(self, money):
        if money > self.balance:
            print('Ошибка')
            raise Exception
        else:
            self.balance -= money

    def get_info(self):
        print(self.balance)

some_account = Bank_akkaynt()
some_account.deposit(money=4)
some_account.winthdraw(money=4)
some_account.get_info()