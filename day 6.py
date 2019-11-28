# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:04:00 2019

@author: Asma Alfauri
"""
from functools import reduce

class Person :
    
    def __init__(self,name:str,address:str):
        self._name=name
        self._address=address
        
    def getName(self):
        return self._name
    
    def setName (self,name):
        self._name=name
        
    def getAddress (self):
        return self._address
    
    def setAddress(self,address):
        self._address=address
        
    def __del__(self):
        print ('I have been deleted')

class Employee(Person):
    
    def __init__(self,employee_number,name,address,salary,job_title,loans):
        super().__init__(name,address)
        self.employee_number=employee_number
        self.__salary=salary
        self.__job_title=job_title
        self.__loans=loans
    
    def getSalary(self):
        return self.__salary
    
    def setSalary (self,salary):
        self.__salary=salary
        
    def getJobTitle(self):
        return self.job_title
    
    def setJobTitle (self,job_title):
        self.__job_title=job_title
        
    def getTotalLoans(self):
        return sum(self.__loans)
    
    def getMaxLoans(self):
        if len(self.__loans) < 1:
            return None
        return max(self.__loans)
    
    def getMinLoans(self):
        if len(self.__loans) < 1:
            return None
        return min(self.__loans)
    
    def setLoans(self,loans):
        self.__loans=loans
        
    def getLoans(self):
        return self.__loans
    
    def __del__(self):
        print ('I have been deleted')
        
    def printInfo(self):
        print (f'''
Employee Number: {self.employee_number}
Employee Name: {self._name}
Employee Address: {self._address}
Employee Salary: {self.__salary}
Employee Job Title: {self.__job_title}
Employee Loans: {self.__loans}
               ''')


class Student(Person):
    
    def __init__(self,student_number,name,address,subject,marks):
        super().__init__(name,address)
        self.student_number=student_number
        self.__subject=subject
        self.__marks=marks
        
    def getSubject(self):
        return self.__subject
    
    def setSubject (self,subject):
        self.__subject=subject
        
    def getMarks(self):
        return self.__marks
    
    def setMarks (self,marks):
        self.__marks=marks
        
    def getAverage(self):
        summation = 0
        length = 0
        for value in self.__marks.values():
            summation += value
            length += 1
        average = summation / length
        return average
    
    def getAMarks(self):
        A_Marks=list(filter(lambda a:a>=90 ,self.__marks.values()))
        return A_Marks
        
    def __del__(self):
        print ('I have been deleted')
        
    def printInfo(self):
        print (f'''
Student Number: {self.student_number}
Student Name: {self._name}
Student Address: {self._address}
Subject: {self.__subject}
Marks: {self.__marks}
               ''')
    

employee1=Employee(1000,'Ahmad Yazan','Amman Jordan',500,'HR Consultant',[434,200,1020])
employee2=Employee(2000,'Hala Rana','Aqaba Jordan',750,'Department Manager',[150,3000,250])
employee3=Employee(3000,'Maram Ali','Mafraq Jordan',600,'HR S Consultant',[304,1000,250,300,500,235])
employee4=Employee(4000,'Yasmeen Mohammad','Karak Jordan',865,'Director',[])


student1 = Student(20191000, 'Khalid Ali', 'Irbid, Jordan', 'History', {
    'english': 80,
    'arabic': 90,
    'art': 95,
    'management': 75
})
student2 = Student(20182000, 'Reem Hani', 'Zarqa, Jordan', 'Software Eng', {
    'english': 80,
    'arabic': 90,
    'management': 75,
    'calculus': 85,
    'os': 73,
    'programming': 90
})
student3 = Student(20161001, 'Nawras Abdulllah', 'Amman, Jordan', 'Arts', {
    'english': 83,
    'arabic': 92,
    'art': 90,
    'management': 70
})
student4 = Student(20172030, 'Amal Raed', 'Tafelah, Jordan', 'Computer Eng', {
    'english': 83,
    'arabic': 92,
    'art': 90,
    'management': 70,
    'calculus': 80,
    'os': 79,
    'programming': 91
})
#Q1...............
EmployeesList=[employee1,employee2,employee3,employee4]

#Q2...............
StudentsList=[student1,student2,student3,student4]

#Q3...............
print (len(EmployeesList))

#Q4...............
print(len(StudentsList))

#Q5..............
for employee in EmployeesList:
    employee.printInfo()
    print ('Employee Total Loans is: ',employee.getTotalLoans())
    
#Q6..............
for student in StudentsList:
    student.printInfo()
    print ('Student Average Marks is: ',student.getAverage())

#Q7..............
highest_Avg=0
for student in StudentsList:
    if highest_Avg < student.getAverage():
        highest_Avg=student.getAverage()
print('The highest average is: ',highest_Avg)

#Q8..............
employee_has_loans = list(filter(lambda e: e.getMinLoans(), EmployeesList))
min_employee_loan = min(list(map(lambda e: e.getMinLoans(), employee_has_loans)))
print ('Employee min Loans is: ', min_employee_loan)

#Q9.............
max_employee_loan = max(list(map(lambda e: e.getMaxLoans(), employee_has_loans)))
print ('Employee max Loans is: ', max_employee_loan)

#Q10............
sum_loans=0
for employee in EmployeesList:
    print (f'''
{employee.getName()} : {employee.getLoans()}
Total loans is: {employee.getTotalLoans()}
           ''')
    sum_loans=sum_loans+employee.getTotalLoans()
print('the total loans for all employees is :',sum_loans)

#Q11............
print(list(map(lambda e: {e.employee_number:e.getLoans()},EmployeesList)))
        
#Q12............
for employee in employee_has_loans:
    max_loan=reduce(lambda a,b :a if a > b else b ,employee.getLoans())
    min_loan=reduce(lambda a,b : a if a < b else b ,employee.getLoans())
    print(employee.getName(),' the max and min loans are : ',max_loan, ', ',min_loan)
    
#Q13...........
students_HasA = list(filter(lambda s: len(s.getAMarks())>0, StudentsList))
for student in students_HasA:
    print(f'''
Name: {student.getName()}
Subject: {student.getSubject()}
Marks: {student.getMarks()}
''')
        
#Q14.........
max_salary=0
for employee in EmployeesList:
    if(employee.getSalary()>max_salary):
        max_salary=employee.getSalary()
print('the max employee salary is: ',max_salary)

#or
# =============================================================================
# employees_salaries = list(map(lambda a: a.getSalary(), EmployeesList))
# max_salary = max(employees_salaries)
# print('Maximum Employee Salary is : ', max_salary)
#         
# =============================================================================
        
#Q15.............
employees_salaries = list(map(lambda a: a.getSalary(), EmployeesList))
min_salary = min(employees_salaries)
print('Minimum Employee Salary is : ', min_salary)    


#Q16...............  
Total_salary=0
for employee in EmployeesList:
    Total_salary=Total_salary+employee.getSalary()
print('the total salaries is: ',Total_salary)

#Q17..............
for employee in EmployeesList:
    del employee
for student in StudentsList:
    del student
        
        
        
        
        
        
        
        
        
        
        