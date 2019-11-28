# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 09:17:07 2019

@author: Asma Alfauri
"""

# =============================================================================
# #Array:
# 
# import numpy as np
# b = np.array([1, 4, 7, 5])
# print('array b is : ',b)
# 
# c = np.array([ [1, 4, 7, 5],[2, 8, 3, 2]])
# print('array c is : ',c)
# 
# a = np.arange(12).reshape(3, 4)
# # arange that mean i need array from 0 to 11
# # reshape that mean re-shape it 3X4
# print('array a is : ',a)
# print ("a size: ", a.size)
# print ("a shape: ", a.shape)
# print ("a ndim: ", a.ndim) 
# #ndin : that mean number of dimention
# print ("a dtype.name: ", a.dtype.name)
# #
# print ("a itemsize: ", a.itemsize)
# #size in baytes
# 
# d = np.array([(1.5,2,3), (4,5,6)])
# print (d)
# print ("d shape: ", d.shape)
# 
# 
# f = np.array( [ [1,2], [3,4] ], dtype=complex )
# print('array f is : ',f)
# 
# e= np.zeros( (4,10) )
# print ('array e is : ',e)
# 
# g= np.ones( (2,4) , dtype=np.int16 )
# print('array g is : ',g)
# 
# i= np.arange( 0, 2, 0.3 )
# print('array i is : ',i)
# 
# j = np.arange(24).reshape(2,3,4)
# print('array j is : ',j)
# print ("j shape: ", j.shape)
# print ("j ndim: ", j.ndim)
# 
# =============================================================================

# =============================================================================
# #Array Operations
# import numpy as np
# a = np.array([1, -1, 7, 3])
# b = np.array([-9, 4, 0, 5])
# c =  np.array([[10, 6, 0, 2],[1,2,3,4]])
# print("a-b: ",a-b)
# print("a*b: ",a*b)
# print("a.dot(b): ",a.dot(b))
# print("a*2: ",a*2)
# print("np.sin(a): ",np.sin(a))
# print("a<3: ",a<3)
# print("a.sum(): ",a.sum())
# print("a.sum(axis=0): ",a.sum(axis=0))
# print("c.sum(): ",c.sum())
# print("c.sum(axis=0): ",c.sum(axis=0))
# #sum element by element and return one dimention array
# #it sum one array to other 
# print("a.min(): ",a.min())
# print("a.max(): ",a.max())
# print("a.mean(): ",a.mean())
# print("a average(): ",np.average(a))
# print("a median(): ",np.median(a))
# print("a std(): ",np.std(a))
# print("a var(): ",np.var(a))
# print("c.cumsum(): ",c.cumsum())
# #التراكمية
# print("a[1:2] :  ",a[1:2])
# print("a[2:] :  ",a[2:])
# print("c[-1] :  ",c[-1])
# #reverse
# =============================================================================

# =============================================================================
# #General
# import numpy as np 
# a = np.array([0,30,45,60,90]) 
# b = np.array([1.0,5.55, 123, 0.567, 25.532]) 
# print ("sin(a): ", np.sin(a*np.pi) )
# print ("b around : ", np.around(b) )
# print ("b around 1: ", np.around(b, decimals = 1) )
# print ( "b around 2: ",np.around(b, decimals = 2) )
# print ("b floor: ", np.floor(b) )
# print ("b ceil: ", np.ceil(b) )
# print ("cos(pi): ", np.cos(np.pi) )
# print ("tan(pi): ", np.tan(np.pi) )
# print ("arcsin: ", np.arcsin(np.pi/180) )
# print ("degrees(pi): ", np.degrees(np.pi) )
# 
# =============================================================================

# =============================================================================
# #Array Operations-Sort
# import numpy as np  
# a = np.array([[3,7,2,1,8,7,19,15],[10,2,7,4,5,5,9,1]]) 
# print('a array:')
# print (a) 
# print('\n quicksort:')
# print (np.sort(a,kind='quicksort') )
# print('\n mergesort')
# print (np.sort(a,kind='mergesort') ) 
# print('\n heapsort:')
# print (np.sort(a,kind='heapsort') ) 
# print('\n sort as flattened arra:')
# print (np.sort(a,axis=None) )
# 
# =============================================================================


# =============================================================================
# #MatPlotlib
#
# import matplotlib.pyplot as plt
# f=[1, 2, 8, 4,5,6]
# plt.plot(f)
# plt.show()
# 
# plt.style.use('ggplot')
# x=[1, 2, 3, 4,5,6]
# y=[1, 4, 9, 16,0,30]
# plt.plot(x,y)
# plt.ylabel('Y Numbers')
# plt.xlabel('X Numbers')
# plt.show()
# 
# =============================================================================

# =============================================================================
# import numpy as np
# import matplotlib.pyplot as plt
# def p1(x):
#     return x**4 -4*x**2 + 3*x 
# def p2(x):
#     return np.sin(10*x) * 10 
# X = np.linspace(-3, 3, 200)
# #create array from -3 to 3 and devided to 200 elements
# plt.plot( X,p1(X), X,p2(X))
# plt.show()
# =============================================================================

# =============================================================================
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(0, 10, 0.005)
# y = np.exp(-x/2.) * np.sin(2*np.pi*x)
# plt.plot(x, y)
# plt.xlim(0, 10)
# plt.ylim(-1, 1)
# plt.show()
# =============================================================================

# =============================================================================
# import numpy as np
# import matplotlib.pyplot as plt
# x=np.arange(0.,10,0.1)
# a=np.cos(x)
# b=np.sin(x)
# c=np.exp(x/10)
# d=np.exp(-x/10)
# plt.plot(x,a,'b-',label='cosine')
# plt.plot(x,b,'r--',label='sine')
# plt.plot(x,c,'g-',label='exp(+x)')
# plt.plot(x,d,'y-',linewidth=5,label='exp(-x)')
# plt.legend(loc='upper left')
# #key of graph
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.show()
# =============================================================================

# =============================================================================
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(0,2, 1000)
# plt.figure()
# 
# plt.plot(x, np.sqrt(x), label = r"Skiing: $\sqrt{x}$")
# plt.plot(x, x**2, label = r"Snowboarding: $x^2$")
 #r that mean draw any thin between $...$ in lable
# plt.title("Learning Curves for Snowboarding and Skiing")
# plt.xlabel("Time")
# plt.ylabel("Skill")
# plt.legend(loc='upper left')
# plt.show
# =============================================================================

# =============================================================================
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(0, 3 * np.pi, 0.1)
# y_sin= np.sin(x)
# y_cos= np.cos(x)
# # Plot the points using matplotlib
# plt.plot(x, y_sin)
# plt.plot(x, y_cos)
# plt.xlabel('x axis label')
# plt.ylabel('y axis label')
# plt.title('Sine and Cosine')
# plt.legend(['Sine', 'Cosine'])
# plt.show()
# 
# =============================================================================

# =============================================================================
# import numpy as np
# import matplotlib.pyplot as plt
# n = 1024
# X = np.random.normal(0,1,n)
# Y = np.random.normal(0,1,n)
# plt.scatter(X,Y)
# plt.show()
# 
# 
# x = np.arange(-2*np.pi,2*np.pi,0.01)
# y = np.sin(3*x)/x
# y2 = np.sin(2*x)/x
# y3 = np.sin(x)/x
# plt.plot(x,y)
# plt.plot(x,y2)
# plt.plot(x,y3)
# =============================================================================

# =============================================================================
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(0, 5, 0.2)
# # red dashes, blue squares and green triangles
# plt.plot(x, x, 'r--', x, x**2, 'bs', x, x**3, 'g^')
# plt.show()
# 
# t = np.arange(0.0, 5.0, 0.01)
# s = np.cos(2*np.pi*t)
# plt.plot(t, s, lw=2)   
# #lw: Line width
# plt.annotate('Max Value', xy=(2, 1), xytext=(3, 1.5),arrowprops=dict(facecolor='black', shrink=0.05))
# plt.ylim(-2,2)
# plt.show()
# =============================================================================

# =============================================================================
# import numpy as np
# import matplotlib.pyplot as plt
# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
# plt.figure(1)
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()
# =============================================================================

# =============================================================================
# import matplotlib.pyplot as plt
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# explode = (0, 0.1, 0, 0)  
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
# ax1.axis('equal')  
# plt.show()
# 
# =============================================================================

# =============================================================================
# import numpy as np
# import matplotlib.pyplot as plt
# def f(x,y): 
#     return (1-x/2+x**5+y**3)* np.exp(-x**2-y**2)
# n = 256
# x = np.linspace(-3,3,n)
# y = np.linspace(-3,3,n)
# X,Y = np.meshgrid(x,y)
# plt.contourf(X, Y, f(X,Y), 8, alpha=.75, cmap='jet')
# plt.contour(X, Y, f(X,Y), 8, colors='black', linewidth=.5)
# plt.show()
# =============================================================================

# =============================================================================
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = Axes3D(fig)
# X = np.arange(-4, 4, 0.25)
# Y = np.arange(-4, 4, 0.25)
# # meshgrid: Return coordinate matrices from coordinate vectors.
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# ax.plot_surface(X, Y, Z, cmap='hot')
# plt.show()
# =============================================================================


#Exercises:
import numpy as np
import matplotlib.pyplot as plt
# =============================================================================
#1
a= np.zeros(10)
b= np.ones(10)
c= np.ones(10)*5
print(f'''
Zeros array is: {a}
Ones array is: {b}
Fives array is:{c}
 ''')
# =============================================================================

# =============================================================================
#2
c= np.arange(30,71,1)
print('array of the integers: ',c)
# =============================================================================

# =============================================================================
#3
d= np.arange(30,71,2)
print('array of the even integers: ',d)
# =============================================================================

# =============================================================================
#4
e=np.identity(3)
print('idenity array: ',e)
# =============================================================================

# =============================================================================
#5
f= np.random.normal(0,1)
print('random number array: ',f)
# =============================================================================

# =============================================================================
#6
g=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
for x in np.nditer(g):
    print('iterate array : ',x, end=' ')
# =============================================================================

# =============================================================================
#7
h=np.arange(21)
print("Original array:")
print(h)
print("New array : ")
h[9:16] = h[9:16]*-1
print(h)
# =============================================================================

# =============================================================================
#8
X=np.array([1,8,3,5])
Y=np.random.randint(0,11,4)
print('multiply 2 vectors : ',X*Y)
# =============================================================================

# =============================================================================
#9
x_matrix=np.array([[1,3,6,7],[6,77,89,90],[5,66,23,22]])
print('the materix is : ',x_matrix)
print('the shape of materix is : ',x_matrix.shape)
# =============================================================================

# =============================================================================
#10
random_matrix=np.random.rand(3,3,3)
print('random matrix 3*3*3',random_matrix)
# =============================================================================

# =============================================================================
#11
a=np.array([9,-1,2,5])
b=np.array([1,-6,0,10])
c=np.array([[1,8,2,5],[3,1,7,9]])
print("a-b: ",a-b) 
print("a*b: ",a*b)
print("a.dot(b):",a.dot(b)) 
print("a*2: ",a*2) 
print("np.sin(a): ",np.sin(a)) 
print("a<3: ",a<3) 
print("a.sum():",a.sum()) 
print("a.sum(axis=0): ",a.sum(axis=0)) 
print("c.sum():",c.sum())
print("c.sum(axis=0): ",c.sum(axis=0)) 
print("a.min(): ",a.min()) 
print("a.max(): ",a.max())
print("a.mean(): ",a.mean()) 
print("a average() ",np.average(a)) 
print("a median(): ",np.median(a)) 
print("a std(): ",np.std(a)) 
print("a var(): ",np.var(a)) 
print("c.cumsum(): ",c.cumsum()) 
print("a[1:2] ",a [1:2]) 
print("a[2:]: ",a [2:]) 
print("c[-1]: ",c[-1] )
# =============================================================================

# =============================================================================
#12
X=np.arange(1,50)
Y=X*3
plt.plot(X,Y)
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
plt.show()
plt.title('Draw a line')
# =============================================================================

# =============================================================================
#13
x1=np.array([10,20,30])
y1=np.array([20,40,10])
x2=np.array([10,20,30])
y2=np.array([40,10,30])


plt.plot(x1,y1,'b-',label='line 1')
plt.plot(x2,y2,'r-',label='line 2')
plt.title('Tow or more lines')
plt.legend(loc='upper right')
plt.show()
# =============================================================================

# =============================================================================
#14

t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'g--', t, t**2, 'bs', t, t**3, 'r^')
plt.show()
# =============================================================================

# =============================================================================
#15
import matplotlib.pyplot as plt
x = ['Python', 'Java', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language")
plt.xticks(x_pos, x)
plt.show()



































































