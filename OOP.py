#basic class and object

"""
class computer:

    def config(self):
        print("new version")

    def feature(self):
        print("new model")

class mobile():

    def version(self):
        print("new mobile")


com1 = computer()
com2 = computer()
mob1 = mobile()



com1.config()
com2.feature()
mob1.version()



"""



#__init__ variable
"""
class computer:

    def __init__(self,ram,cpu):
        self.ram = ram
        self.cpu = cpu

    def configur(self):
        print("hello computer")
        print("you have inside :",self.ram,self.cpu)

com1 = computer('i7',16)

com1.configur()
"""

"""
#constructor and self

class person:
    def __init__(self):
        self.name  = "nayeem"
        self.age  = 24

    def update(self):
        self.age = 25
        
    def iscompare(self,p2):
        if self.age == p2.age:
            return True
        else:
            return False

p1 = person()
p2 = person()

p1.update()

if p1.iscompare(p2):
    print("they are same")
else:
    print("they are different")

"""
#constructor , self , compare
"""
class person:
    def __init__(self):
        self.name = 'nayeem'
        self.age = 23

    def update(self):
        self.age = 25

    def iscompare(self,p2):
        if self.age == p2.age:
            return True
        else:
            return False


p1 = person()
p2 = person()

p2.update()

if p1.iscompare(p2):
    print("they are same")
else:
    print("they are different")

print(p1.name)
print(p2.age)
"""

#types of variable
     #class  : we can't change the value
     #instance : we can change the value

"""
class car:

    wheels = 4

    def __init__(self):    #instance
        self.name = "bmw"
        self.mil = 20

c1 = car()
c2 = car()

car.wheels = 5

print(c1.name,c1.mil,c1.wheels)
print(c2.mil,c2.mil,c2.wheels)


"""


"""

#types of method
        #instance
        #class
        #static


class school:

    name = 'ping pong school'

    def marks(self,m1,m2,m3):
        self.m1 = m1;
        self.m2 = m2;
        self.m3 = m3;

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    @classmethod
    def getname(cls):
        return cls.name

    @staticmethod
    def info():
        print("heyu hoi hi hi bye")



m = school()
m.marks(30,30,30)
print(m.avg())
print(school.getname())
school.info()

"""

"""
class student:
    school = "ping pong school"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return ((self.m1 + self.m2 + self.m3) / 3)

    @classmethod
    def getname(cls):
        return cls.school

    @staticmethod
    def info():
        print("they belongs to same school")


s = student(10, 20, 30)
print(s.avg())
print(student.getname())
student.info()

"""



"""
#inner class python

""""""
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.lap = self.laptop()

    def show(self):
        print(self.name,self.age)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand = 'asus'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = student('nayeem',23)
s1.show()
"""

#class inside a class

"""
class school :
    def __init__(self,id,name):
        self.name = name
        self.id = id
        self.d = self.depart()

    def show(self):
        print(self.id,self.name)
        self.d.show()


    class depart:
        def __init__(self):
            self.id = '171'
            self.name = 'cse'
            self.place= 'corner'

        def show(self):
            print(self.id,self.name,self.place)

s = school(145,'iubat')
s.show()


"""



#introduction to inheritence

"""
class A:

    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")

class B:

    def feature3(self):
        print("feature 1 is working")

    def feature4(self):
        print("feature 2 is working")


class C(A,B):

    def feature5(self):
        print("feature 3 is working")

    def feature6(self):
        print("feature 4 is working")

b = B()
b.
c = C()
c.

"""

# constructor in inheritence in python

"""
class A:

    def __init__(self):
        print('constructor from class A')

    def model1(self):
        print('hey I am from model1')

    def model2(self):
        print('hey i am form model2')

class B(A):

    def __init__(self):
        super().__init__()
        print('constructor from class B')
    
    def model3(self):
        print('i am from model 3')
        
    def model4(self):
        print('i am from model 4')

a = B()

"""
#why python supports multiple inheritence
#MRO = method resulation order


"""
class A:

    def __init__(self):
        print('constructor init from A')

    def feature1(self):
        print("feature 1-A is working")

    def feature2(self):
        print("feature 2 is working")

class B:

    def __init__(self):
        print('constructor init from B')

    def feature1(self):
        print("feature 1-B is working")

    def feature1(self):
        print("feature 1-nothing is working")

    def feature4(self):
        print("feature 4 is working")

class D:
    
    def __init__(self):
        print("constructor from D")



class C(D,A,B):

    def __init__(self):
        super().__init__()
        print('constructor init from C')

    def feature5(self):
        print("feature 5 is working")

    def feature6(self):
        print("feature 6 is working")

    def feat(self):
        super().feature4()

a = C()
a.feature1()
a.feat()
"""




#polymorphism
#Duck typing in python

"""

class pycharm:
    
    def execute(self):
        print("running")
        print("compiling")

class myeditor:

    def execute(self):
        pc.execute()
        print("spelling mistake")
        print("convention check")



class laptop:

    def code(self,ide):
        ide.execute()


id = myeditor()
pc = pycharm()

lap1 = laptop()
lap1.code(id)

"""



"""
class shoppingmall:

    def execute(self):

        print("pant")
        print("shirt")

class dokan:

    def execute(self):
        sp.execute()
        print("ada")
        print("moida")

class shop:

    def shelf(self,ide):
        ide.execute()

ide = dokan()
sp = shoppingmall()

s = shop()
s.shelf(ide)

"""

#polymorphism
#operator overloading
"""
class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2


    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3

    
    def __str__(self):
        return '{} {}'.format(self.m1 , self.m2)


    def __gt__(self, other):
          s1 = self.m1 + self.m2
          s2 = self.m2 + self.m2

          if s1>s2 :
              return True
          else:
              return False
s1 = student(10,20)
s2 = student(15,22)

s3  = s1 + s2
print(s3)

if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")

"""


"""
class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        s1 = self.m1 + other.m1
        s2 = self.m2 + other.m2
        s3 = student(s1,s2)
        return s3


    def __gt__(self, other):

        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1>r2:
            return True
        else:
            return False

    

    def __str__(self):
          return '{} {}'.format(self.m1,self.m2)



s1 = student(10,20)
s2 = student(12,20)

s3 = s1 + s2
print(s3)

if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")

"""




#method overloading

"""
class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def sum(self,x = None,y = None,z =None):

        sum = 0
        if x!=None and y!=None and z!=None:
            sum = x+y+z

        elif x!=None and y!=None:
            sum = x+y

        else:
            sum = x

        return sum

s = student(10,20)
print(s.sum(10))

"""


#method overriding

"""
class A:
    def show(self):
        print("A here")

class B(A):
    def show(self):
        print("B here")

a = B()
a.show()

"""


"""
n = int(input())
name = []
for j in range(0,n):
        ele = input()
        name.append(ele);
print(name)

"""

"""

#abstraction in python
from abc import ABC,abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass

class laptop(computer):
    def process(self):
        print("its running")

class programmer:
    def work(self):
        print("solving bugs")
        lap.process()

lap = laptop()
prog = programmer()
prog.work()

"""

#iteration in python

"""
nums = [1,2,5,8]
#print(nums[2])
# for i in nums:
#     print(i)

# it = iter(nums)
# print(it.__next__())
# print(it.__next__())
# for i in nums:
#      print(i)

it = iter(nums)
print(next(it))
print(next(it))

"""

#iteration by using class and object


"""
class topten:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <=10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

t = topten()
print(next(t))

for i in t:
     print(i)
     
"""

"""
class topten:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
            val= self.num
            self.num +=1
            return val
        else:
            raise StopIteration
        
t = topten()

print(next(t))

for i in t:
    print(i)
"""
"""
class topten:
    def __init__(self):
        self.val = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.val<=10:
            nums = self.val
            self.val +=1
            return nums
        else:
            raise StopIteration

values = topten()
for i in values:
    print(i)
"""


#generators in python


"""
def topten():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n +=1
values = topten()
print(next(values))

for i in values:
    print(i)
"""

# nums = [1,5,4,8,4]
# it =  iter(nums)
# print(next(it))
# print(next(it))
# for i in nums:
#     print(i)



"""
"""
"""
def topten():
    yield 1
    yield 2
    yield 3
    yield 4

values = topten()
print(next(values))
print(next(values))
for i in values:
    print(i)

"""
"""
def topten():

    n = 1

    while(n<=10):
        sq = n * n
        yield sq
        n +=1

values = topten()
for i in values:
    print(i)
 

"""




"""
n = int(input())
for i in range(0,n):
    a, b = map(int, input().split())
    print(a,b)

"""
"""
n = int(input())
for i in range(0,n):
    a,b = map(int,input().split())

try:

    print("resources open")
    print(a/b)

    x = int(input())
    print(x)


except ZeroDivisionError as e:
    print("division by zero error",e)

except ValueError as e:
    print("value error by the user",e)

except Exception as e:
    print("wrong input")

finally:
    print("resources closed")

print("bye bye")


"""

"""

#multithreading

from abc import ABC,abstractmethod

from time import sleep
from threading import *


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)



h1 = Hello()
h2 = Hi()

h1.start()
sleep(0.2)
h2.start()

h1.join()
h2.join()

print("bye bye")

"""

  














    






































