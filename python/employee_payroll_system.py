"""
[
    {
        "name": "John Wick",
        "designation": "Pet Gaurd",
        "salary": 100000
    },
    {
        "name": "John Wick",
        "designation": "Pet Gaurd",
        "salary": 100000
    },
]
"""

employees = []

def add_employee():
    # Getting Details
    name = input("Employee Name: ")
    designation = input("Designation: ")
    salary = int(input("Salary: "))

    # Creating Employee record
    employee = {
        "name": name,
        "designation": designation,
        "salary": salary
    }

    # adding it to the employee list
    employees.append(employee)

def list_employees():
    # Printing headings
    print("Name\tDesignation\tSalary")
    
    # ittrating employees list
    for employee in employees:

        # printing each employee record
        print(f"{employee['name']}\t{employee['designation']}\t\t{employee['salary']}")

def update_employee():
    employee_name = input("Name of the Employee you want to update: ")

    # ittrating employees list
    for employee in employees:
        if employee_name == employee['name']:
            # Getting Details
            name = input("Employee Name: ")
            designation = input("Designation: ")
            salary = int(input("Salary: "))

            # Updating Employee record
            employee['name'] = name
            employee['designation'] = designation
            employee['salary'] = salary
            
            print("Success: Employee Updated! ")
            return

    # printing each employee record
    print(f"Error: {employee_name} is not existed! ")

def search_employee():
    employee_name = input("Name of the Employee you want to Search: ")

    # ittrating employees list
    for employee in employees:
        if employee_name == employee['name']:
            print("Name\tDesignation\tSalary")
            print(f"{employee['name']}\t{employee['designation']}\t\t{employee['salary']}")
            return

    # printing each employee record
    print(f"Error: {employee_name} is not existed! ")

def delete_employee():
    employee_name = input("Name of the Employee you want to Delete: ")

    # ittrating employees list
    for index, employee in enumerate(employees):
        if employee_name == employee['name']:
            employees.pop(index)
            return

    # printing each employee record
    print(f"Error: {employee_name} is not existed! ")

def calc_total_salaries():    
    total_salaries = 0
    for employee in employees:
        total_salaries += employee['salary']
        
    print(f"Total Monthly Salary Expenses are {total_salaries}")

choice = 1
while choice > 0:
    print("\n\n")
    print("Add Employee Press 1")
    print("Update Employee Press 2")
    print("Delete Employee Press 3")
    print("Search Employee Press 4")
    print("List Employees Press 5")
    print("Calulate Total Salaries Press 6")
    print("For Exit Press 0")

    choice = int(input("\n\nPlease select a manu: "))
    print("\n\n")


    if choice == 1:
        add_employee()
    elif choice == 2:
        update_employee()
    elif choice == 3:
        delete_employee()
    elif choice == 4:
        search_employee()
    elif choice == 5:
        list_employees()
    elif choice == 6:
        calc_total_salaries()
    elif choice == 0:
        print("exiting the program....")
    else:
        print("Invalid input, select again from the manu please ")
    