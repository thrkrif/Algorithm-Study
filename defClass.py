# def
a = 1

# def vartest(a):
#     a = a + 1
#     return a

# a = vartest(a)
# print(a)

# # lamda

# add = lambda a,b:a+b
# result = add(3,4)
# print(result)

# """ number = input()
# print(number)
# print(type(number)) """

# for i in range(1,10):
#     print(i, end=' ')

def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result

print(avg_numbers(1,2,3))
print(avg_numbers(1,2,3,4,5))

print("".join(['you','need','python']))

class Fourcal():
    def __init__(self,a,b):
        self.data1 = a
        self.data2 = b
    def setData(self,a,b):
        self.data1 = a
        self.data2 = b
    def add(self):
        self.result = self.data1 + self.data2
        return self.result
    
a = Fourcal(1,1)
a.setData(4,2)
print(a.add())

b = Fourcal(5,10)
print(b.add())

class moreFourcal(Fourcal):
    def pow(self):
        self.result = self.data1 ** self.data2
        return self.result
    
k = moreFourcal(4,2)
print(k.pow())

