# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 09:18:45 2019

@author: Asma Alfauri
"""
"""
def my_function  ():
    print ("Hello from a function")
    

my_function()
my_function()

def my_function1  (fname):
    print (fname + " Hello from a function")

my_function1("Asma")
my_function1("Sama")


def my_function2  (fname="Asma"):
    #defult value Asma
    print (fname + " Hello from a function")

my_function2("Ahmad")
my_function2("Sama")
my_function2()



def my_function3  (food):
    for x in food:
        print (x)
fruits=["apple" , "banana","cherrey"]
my_function3(fruits)


def my_function4  (x):
    return 5 * x
print (my_function4(3))



def my_function5  (child3, child2, child1):
    print ("the youngest child is " +child3)
my_function5("sam","huda","khalid")
my_function5(child1="sam",child3="huda",child2="khalid")


def adder (x,y,z):
    print ("Sum = " , x+y+z)
adder (10,12,3)


def adder2(*num):
    #multi values
    sum = 0
    for n in num:
        #type of num is tuple
        sum=sum + n
    print ("SUM = " , sum)
adder2(2,3,4)
adder2(3,15,4,72,96)


def myfun (arg1,*argv):
    print("first agrument is : ", arg1)
    for arg in argv:
        print ("Next arguments through *argv :",arg)
myfun('Hello','welcome','to','greek')

"""
"""
def myfun2 (*argv,arg1):
    for arg in argv:
        print ("Next arguments through *argv :",arg)
    print("first agrument is : ", arg1)
myfun2('Hello','welcome','to','greek')
#must be order from single agrument to up
"""
"""
def area_triangle (*args):
    return args[0]*args[1]/2
print ("the area of triangle is =" ,area_triangle (10,30))

"""
"""
def  area_triangle(base,height):
    return base*height/2
"""
"""
def some_args(arg1,arg2,arg3):
    print ("arg1: ",arg1)
    print ("arg2: ",arg2)
    print ("arg3: ",arg3)
my_list =[2,3]
args=("tow",3)
some_args(1,*my_list)
print("*******")
some_args(1,*args)


def myfun3(**kwargs):
    # the ** that means key and value
    for key,value in kwargs.items():
        print ("%s == %s" %(key ,value))
myfun3(first='geeks',mid='for',last='geeks')


x="awesome"
def myfun4():
    x="fantastic"
    print("local variabl is "+x)
myfun4()
print("global variable is "+x)


x="awesome"
def myfun5():
    print("local variabl is "+x)
myfun5()
print("global variable is "+x)


x = "awesome"
def myfun6():
    global x
    x = "fantastic"

print ("x before call function is = " , x)
myfun6()
print ("x after call function is = " , x)


def factorial (n):
    if n ==1:
        return 1
    else:
        return n * factorial (n-1)
    
print(factorial(1))
print(factorial(4))
print(factorial(100))


sum = lambda x, y, z : x + y + z
print (sum(5,75,3))

x1= (lambda x, y: x + y)(2, 3)
print(x1)

print((lambda x, y: x + y)(2, 3))

print ((lambda x, y, z=3: x + y + z)(1, 2))
print ((lambda x, y, z=3: x + y + z)(1, 2,5))


my_pets=["a","b","c","d"]
uppered_pets=list(map(str.upper,my_pets))
print (uppered_pets)

print(list(map(lambda x: x.upper(), ['cat', 'dog', 'cow'])))

li=[2,4,6,8,10]
multiply_li=list(map(lambda x:x*2 ,li))
power2_li=list(map(lambda x:x**2 , li))
print ("my list is = " ,li)
print ("my list *2 = ",multiply_li)
print ("my list power 2 = " ,power2_li)


def multiply_list (*li):
    for x in li:
        return x*2
print (multiply_list (li))


circle_areas= [3.56773, 5.57668, 4.00914, 56.242444441, 9.40134444440, 32.000155555555555]
result = list(map(round, circle_areas, range(1,7)))
print(result)



sentence = 'AlZytonah University of Jordan '
print ( list(map(lambda x: len(x), sentence.split()) ) )


filtered = list( filter(lambda x: x % 2 == 0, range(0,12)))
print(filtered) 


MyList= [0,1,2,3,4,10,13,22,25,100,120]
odd_numbers= list(filter(lambda x: x % 2, MyList))
print(odd_numbers)
even_numbers= list(filter(lambda x: x % 2 == 0, MyList))
print(even_numbers)
over50=list(filter(lambda x:x>50 , MyList))
print(over50)


scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
over_75=list(filter(lambda x:x>75 , scores))
print (over_75)


my_strings= ['a', 'b', 'c', 'd', 'e']
my_numbers= [1,2,3,4,5]
my_names=['asma','shaker','Abdullah']
results = list(zip(my_strings, my_numbers,my_names))
print(results)



from functools import reduce

#to import reduce labrary for one time
# in each project not in each function

x= reduce(lambda a,b: a+b,[23,21,45,98])
print(x)


import functools
# initializing list 
lis= [ 1 , 3, 5, 6, 2]
 # using reduce to compute sum of list 

print ("The sum of the list elements is : ",end="") 

print (functools.reduce(lambda a,b: a+b,lis))
 # using reduce to compute maximum element from list
print ("The maximum element of the list is : ",end="")
print (functools.reduce(lambda a,b: a if a > b else b,lis))


"""

#exercise

#exercise 1
o=lambda x=1,y=2,z=3: x+y+z

print(o())
print(o(10)) #replace the z value to 10
print(o(10,20))

#exercise 2
list1=[1,2,3,4,5,6]
from functools import reduce
x= reduce(lambda a,b: a*b,list1)
print(x)

#or 

def multiply_list (*list1):
    y=1
    for x in list1 :
        y=y*x
    return (y)
    
print("multiply_list" ,multiply_list(2,4,6))
        

#excersise 3
x1= (lambda x, y: x * y)(2, 3)
print(x1)

#excersise 4
z =list(filter(lambda x: x<0, range(-5,5)))
print(z) 

#excersise 5
x = lambda a, b, c : a + b + c 
print(x(5, 6, 2))
# the answer is 13

#excersise 6
x=("Joey", "Monica", "Ross")
y=("Chandler", "Pheobe")
z=("David", "Rachel", "Courtney") 
result = list(zip(x, y, z)) 
print(result)
#the answer is [('Joey', 'Chandler', 'David'), ('Monica', 'Pheobe', 'Rachel')]

#excersise 7
coin=('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC') 
d = dict(zip(coin, code))
print(d)
#the answer is {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}

#excersise 8

def func(variable):
    letters=['a','e','o','u']
    if (variable in letters):
        return True
    else :
        return False
sequence=['g','j','e','j','k','o','p','r']
filtered=list(filter(func,sequence))
print (filtered)
#the answer is ['e', 'o']

#excersise 9
'''
x=list(map(int,input("Enter a multiple value: ").split()))
print("list of student: ",x)
#the answer is Enter a multiple value:  1 20 10 list of student:  [1, 20, 10]
'''
#excersise 10
def newfunc(a):
    return a*a
x=list(map(newfunc,(1,2,3,4)))
print(x)
#the answer is [1, 4, 9, 16]

#exercise 11
def fun(a,b):
    return a+b
a=list(map(fun,[2,4,5],[1,2,3,4]))
print(a)
#the answer is [3, 6, 8]

#exercise 12
c=map(lambda x:x+x,filter(lambda x:(x>=3),(1,2,3,4)))
print(list(c))
#the answer is [6, 8]

#exercise 13
c=filter(lambda x:(x>=3),map(lambda x:x+x,(1,2,3,4)))
print(list(c))
#the answer is [4, 6, 8]

#exercise 14
import functools
my_list=[1,3,4,15,16,85,792]
print (functools.reduce(lambda a,b: a if a < b else b,my_list))

#exercise 15
numbers=[1,2,3]
letters=['a','b','c']
result=list(zip(numbers,letters))
print (result)

























































































































































