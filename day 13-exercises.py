import sqlite3
from tkinter import *
from tkinter import scrolledtext



class Employee:
    def __init__(self):
        self.__conn = sqlite3.connect('project3.db')
        self.__c = self.__conn.cursor()

        data = """CREATE TABLE IF NOT EXISTS employees (
                        number int, name text, gender text,
                        nationality text, dob text, address text,
                        department text, salary real )
        """
        self.__c.execute(data)
        self.__conn.commit()

    def add_row(self, employee: {}):
        data = f""" INSERT INTO employees VALUES (
             {employee["number"]},
             '{employee["name"]}',
             '{employee["gender"]}',
             '{employee["nationality"]}',
             '{employee["dob"]}',
             '{employee["address"]}',
             '{employee["department"]}',
             {employee["salary"]}
        )"""
        self.__c.execute(data)
        self.__conn.commit()

    def get_row(self, columns='*', condition=""):
        data = f"SELECT {columns} from employees {condition}"
        rows = self.__c.execute(data)
        return list(rows)

    def __del__(self):
        self.__conn.close()

class view:
    def __init__(self):
        self.__c = Tk()
        self.__c.title('Main window')
        self.__c.geometry('200x200')

        Button(self.__c, text="Add New Employee", command=self.add_window).grid()
        Button(self.__c, text="View Employees", command=self.view_employees).grid()
        

        self.__c.mainloop()

    def add_window(self):
        c = Toplevel(self.__c)
        c.title('Add New Employee')
        c.geometry('700x500+500+100')
        Label(c, text="Add New Employee").grid()

        number = Label(c, text="Number").place(x=30, y=40)
        name = Label(c, text="Name").place(x=30, y=60)
        gender = Label(c, text="Gender").place(x=30, y=80)
        nationality = Label(c, text="Nationality").place(x=30, y=100)
        dob = Label(c, text="DOB").place(x=30, y=120)
        address = Label(c, text="Address").place(x=30, y=140)
        department = Label(c, text="Department").place(x=30, y=160)
        salary = Label(c, text="Salary").place(x=30, y=180)

        number_value = IntVar()
        name_value = StringVar()
        gender_value = StringVar()
        nationality_value = StringVar()
        dob_value = StringVar()
        address_value = StringVar()
        department_value = StringVar()
        salary_value = IntVar()

        Entry(c, textvariable=number_value).place(x=100, y=40)
        Entry(c, textvariable=name_value).place(x=100, y=60)
        Entry(c, textvariable=gender_value).place(x=100, y=80)
        Entry(c, textvariable=nationality_value).place(x=100, y=100)
        Entry(c, textvariable=dob_value).place(x=100, y=120)
        Entry(c, textvariable=address_value).place(x=100, y=140)
        Entry(c, textvariable=department_value).place(x=100, y=160)
        Entry(c, textvariable=salary_value).place(x=100, y=180)

        def save_employee():
            employees = Employee()
            employees.add_row({
                "number": number_value.get(),
                "name": name_value.get(),
                "gender": gender_value.get(),
                "nationality": nationality_value.get(),
                "dob": dob_value.get(),
                "address": address_value.get(),
                "department": department_value.get(),
                "salary": salary_value.get()
            })

        Button(c, text="Save", command=save_employee).place(x=30, y=200)

    def view_employees(self):
        c = Toplevel(self.__c)
        c.title('View Employees')
        c.geometry('700x500+510+110')
        Label(c, text="View Employee").grid()

        employees = Employee()
        rows = employees.get_row()

        data = 'Number \t\t Name \t\t Gender \t\t Nationality \t\t DOB \t\t Address \t\t Department \t\t Salary \n'
        Label(c, text=data).grid()

        for employee in rows:
            row = f"{employee[0]} \t\t {employee[1]} \t\t {employee[2]} \t\t {employee[3]} \t\t " \
                     f"{employee[4]} \t\t {employee[5]} \t\t {employee[6]} \t\t {employee[7]} \n"
            Label(c, text=row).grid()




windows = view()