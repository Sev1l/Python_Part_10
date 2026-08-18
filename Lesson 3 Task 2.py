## Object oriented programming techniques
# Task 2 (Simple date)


class SimpleDate:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year
        self.result = str(self.day) + "." + str(self.month) + "." + str(self.year)
    def __str__(self):
        return f'{self.result}'
    def __eq__(self,another):
        return (self.year, self.month, self.day) == (another.year, another.month, another.day)
    def __ne__(self,another):
        return (self.year, self.month, self.day) != (another.year, another.month, another.day)
    def __lt__(self,another):
        return (self.year, self.month, self.day) < (another.year, another.month, another.day)
    def __gt__(self,another):
        return (self.year, self.month, self.day) > (another.year, another.month, another.day)
    def __add__(self,another):
        summ = self.day + another
        year = self.year + summ // 365
        summ = summ % 365
        month = self.month + summ // 30
        year += month // 12
        month = month % 12
        summ = summ % 30
        return SimpleDate(summ,month,year)
d1 = SimpleDate(4, 10, 2020)
d2 = SimpleDate(28, 12, 1985)
d3 = SimpleDate(28, 12, 1985)
print(d1)
print(d2)
print(d1 == d2)
print(d1 != d2)
print(d1 == d3)
print(d1 < d2)
print(d1 > d2)
print()
d1 = SimpleDate(4, 10, 2020)
d2 = SimpleDate(28, 12, 1985)
d3 = d1 + 3
d4 = d2 + 400
print(d1)
print(d2)
print(d3)
print(d4)
