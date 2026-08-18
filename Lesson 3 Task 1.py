## Object oriented programming techniques
# Task 1 (Money)


class Money:
    def __init__(self,first,second):
        self.first = str(first)
        self.second = str(second)
        if len(self.second) == 1:
            self.second = "0" + self.second
        self.total = self.first + "." + self.second
        self.res = round(float(self.total),2)
    def __str__(self):
        return f'{self.res} eur'
    def __eq__(self,another):
        return self.total == another.total
    def __ne__(self,another):
        return self.total != another.total
    def __lt__(self,another):
        return self.total < another.total
    def __gt__(self,another):
        return self.total > another.total
    def __add__(self,another):
        result = float(self.total) + float(another.total)
        result = str(result)
        fir1 = ''
        sec2 = ''
        k = 0
        for i in range(len(result)):
            if result[i] != ".":
                fir1 += result[i]
            else:
                k = i
                break
        sec2 = result[k+1:]
        fir = int(fir1)
        sec = int(sec2)
        return Money(fir,sec)
    def __sub__(self,another):
        result = float(self.total) - float(another.total)
        if result < 0:
            raise ValueError('a negative result is not allowed')
        else:
            result = str(result)
            fir1 = ''
            sec2 = ''
            k = 0
            for i in range(len(result)):
                if result[i] != ".":
                    fir1 += result[i]
                else:
                    k = i
                    break
            sec2 = result[k+1:]
            fir = int(fir1)
            sec = int(sec2)
            return Money(fir,sec)
            
    
        
    
e1 = Money(4, 5)
e2 = Money(2, 95)
e3 = e1 + e2
e4 = e1 - e2
print(e3)
print(e4)

try:
    e5 = e2 - e1
    print(e5)
except ValueError as e:
    print(f"ValueError: {e}")
