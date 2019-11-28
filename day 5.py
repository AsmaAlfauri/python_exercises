# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 09:24:33 2019

@author: Asma Alfauri
"""


# =============================================================================
# class Person:
#     def say_hello(self):
#        print('Hello')
# p = Person()
# p.say_hello()
# =============================================================================


# =============================================================================
# class Person:

#     #constructor or initializer
#     def __init__(self,name):
#         self.name=name

#     #metod which returns a string
#     def whoami(self):
#         return "I'm " + self.name

#     #destructors
#     def __del__(self):
#         print ("I have been deleted")
# 
# p1=Person('Tom')
# print(p1.whoami())
# print(p1.name)
# del p1
# =============================================================================

# =============================================================================
# class Encapsulation(object):
#     def __init__(self, a, b, c):
#         self.Apublic= a
#         self._Bprotected= b
#         self.__Cprivate= c
#         
#     def getprivate(self):
#         return self.__Cprivate
#     
#     def setprivate(self,value1):
#         self.__Cprivate=value1
# 
# x = Encapsulation(11,13,17)
# print ( x.Apublic)
# print ( x._Bprotected)
# #print ( x.__Cprivate) 
# #AttributeError: 'Encapsulation' object has no attribute '__Cprivate'
# print ( x.getprivate()) 
# #this is method to get access to private methods
# x.setprivate(1)
# #this way to get access to edit the private methods value
# print ( x.getprivate())
# =============================================================================
# 
# =============================================================================
# class Parent(object):
#     def __init__(self , name, age, salary):
#         self.name=name
#         self._age=age
#         self.__salary=salary
#         
#     def public(self):
#         print("calling public")
#         
#     def _protected(self):
#         print("calling protected")
#     
#     def __private(self):
#         print("Is it really private?")
#     
# class Child(Parent):
#     def foo(self):
#         self.public()
#         self._protected()
#         print(self.name)
#         print(self._age)
# 
# c=Child("Hussam",40,100)
# c.foo()
# c.public()
# =============================================================================

# =============================================================================
# class MySuperClass1():
#     def method_super1(self):
#         print("method_super1 method called")
# 
# class ChildClass(MySuperClass1):
#     def child_method(self):
#         print("child method")
# c = ChildClass()
# c.method_super1()
# c.child_method()
# =============================================================================

# =============================================================================
# class A(object):
#     def __init__(self):
#         print("world")
#         
# class B(A):
#     def __init__(self):
#         print("hello")
# b1=B()
# #the proraity for B not A 
# =============================================================================

# =============================================================================
# class A(object):
#     def __init__(self):
#         print("world")
# class B(A):
#     def __init__(self):
#         print("hello")
#         super().__init__()
#         #to call the A init way 1
#         A.__init__(self)
#         #to call the A init way 2
# b1=B()
# =============================================================================

# =============================================================================
# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length * self.width
#     
#     def perimeter(self):
#         return 2*self.length +2 * self.width
# 
# class Square(Rectangle):
#     def __init__ (self,length):
#         super().__init__(length,length)
# 
# class Cube(Square):
#     def surface_area(self):
#         face_area=super().area()
#         return face_area *6
#     def volume(self):
#         face_area=super().area()
#         return face_area * self.length
#     
# c=Cube(2)
# print(c.surface_area())
# print(c.volume())
# =============================================================================

# =============================================================================
# class MySuperClass1():
#     def method_super1(self):
#         print("method_super1 method called")
# 
# class MySuperClass2():
#     def method_super2(self):
#         print("method_super2 method called")
#         
# class ChildClass(MySuperClass1, MySuperClass2 ):
#     def child_method(self):
#         print("child method")
# 
# c = ChildClass() 
# c.method_super1() #method_super1 method called
# c.method_super2() #method_super2 method called
# c.child_method() #child method
# =============================================================================

# =============================================================================
# class A():
#     def __init__(self):
#         self.__x= 1
#     def m1(self):
#         print("m1 from A")
#         
# class B(A):
#     def __init__(self):
#         self.__y= 1
#     def m1(self):
#         print("m1 from B")
# c = B()
# c.m1() #take the last one
# =============================================================================

# =============================================================================
# # Create Class Vehicle
# class Vehicle:
#     def print_details(self):
#         print("This is parent Vehicle class method")
# 
# # Create Class Car that inherits Vehicle
# class Car(Vehicle):
#     def print_details(self):
#         print("This is child Car class method")
# 
# # Create Class Cycle that inherits Vehicle
# class Cycle(Vehicle):
#     def print_details(self):
#         print("This is child Cycle class method")
# 
# car_a= Vehicle()
# car_a. print_details()
# 
# car_b= Car()
# car_b.print_details()
# 
# car_c= Cycle()
# car_c.print_details()
# =============================================================================

# =============================================================================
# #OperatorOverloading example 
#
# class Circle:
#     def __init__(self, radius):
#         self.__radius= radius
#     
#     def setRadius(self, radius):
#         self.__radius= radius
#         
#     def getRadius(self):
#          return self.__radius
#      
#     def __add__(self, another_circle):
#         return Circle( self.__radius+ another_circle.__radius)
#     
# c1 = Circle(4)
# print(c1.getRadius())
# c2 = Circle(5)
# print(c2.getRadius())
# c3 = c1 + c2 
# print(c3.getRadius())
# =============================================================================

# =============================================================================
# #Local Variables:
# 
# class Car:
#     def start(self):
#         message = "Engine started"
#         return message
# car_a= Car()
# print(car_a.start())
# #start is global in perant
# 
# class Car1:
#     def start(self):
#         message = "Engine started"
#         return message
# car_a1= Car1()
# print(car_a1.message) #AttributeError: 'Car1' object has no attribute 'message'
# #message is local attribute
# =============================================================================

# =============================================================================
# #Class and Instance Variables:
# 
# class Dog:
#     kind = 'canine'
#     # class variable shared by all instances
#     def __init__(self, name):
#         self.name = name    
#         # instance variable unique to each instance
# 
# d = Dog('Fido') 
# e = Dog('Buddy')
# print( d.kind) # shared by all dogs =canine
# print(e.kind)  # shared by all dogs =canine
# print(d.name ) # unique to d =Fido
# print(e.name ) # unique to e =buddy
# d.kind= "e" #now the kind in d object is equal to 'e' but kind at e object still equal 'canine' 
# print( d.kind) #e                
# print(e.kind)  #canine
# =============================================================================


#exercises:

#exercise 1:
class Employee:
    def __init__(self,employee_number,name,address,salary,job_title):
        self.employee_number=employee_number
        self.__name=name
        self.__address=address
        self.__salary=salary
        self.__job_title=job_title
    
    def getName(self):
        return self.__name
    def getAddress(self):
        return self.__address
    def setAddress(self,address):
        self.__address=address
    def getSalary(self):
        return self.__salary
    def getJobTitle(self):
        return self.__job_title
    def __del__(self):
        print (self.__name ," I have been deleted")

Employee1=Employee(1,'Mohammed Khalid',"Amman,Jordan",500,"Consultant")
Employee2=Employee(2,"Hala Rana","Aqaba , Jordan",750,"Manager")

print ("Employee number : "  ,Employee1.employee_number)
print ("Name : " , Employee1.getName())
print ("Address : " , Employee1.getAddress())
print ("Salary : " , Employee1.getSalary())
print ("Job Title : " , Employee1.getJobTitle())

print ("Employee number : "  ,Employee2.employee_number ,",Name : " , Employee2.getName(),",Address : " , Employee2.getAddress(),",Salary : " , Employee2.getSalary(),",Job Title : " , Employee2.getJobTitle())

Employee2.setAddress('USA')
print('Employee1 New Adress: ',Employee2.getAddress())
del Employee1
del Employee2


    










































































































