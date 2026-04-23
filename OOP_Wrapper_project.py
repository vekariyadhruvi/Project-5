employees=[]
print("--- Python OOP Project: Employee Management System ---")

class Employee:
    def __init__(self, name, age, employee_id, salary):
        self.name= name
        self.age= age
        self.__employee_id= employee_id
        self.__salary= salary

    def get_employee_id(self):
        return self.__employee_id
    
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary:$", str(self.__salary))

class Manager(Employee):
    def __init__(self, n, a, eid, sal, dep):
        super().__init__(n, a, eid, sal)
        self.department= dep

    def display(self):
        super().display()
        print("Department:", self.department)

class Developer(Employee):
    def __init__(self, n, a, eid, sal, lan):
        super().__init__(n, a, eid, sal)
        self.language= lan

    def display(self):
        super().display()
        print("Programming Language:", self.language)


while True:
    print("\nChoose an operation:")
    print("1. Create an Employee")
    print("2. Create a Manager")
    print("3. Create a Developer")
    print("4. Show Details")
    print("5. Exit")

    choice=int(input("\nEnter your choice:"))

    if choice==1:
        n=input("Name: ")
        a=input("Age: ")
        eid=input("Employee ID: ")
        sal=float(input("Salary: $"))
        employees.append(Employee(n, a, eid, sal))
        print(f"Employee created with Name:{n}, Age:{a}, Employee ID:{eid}, Salary:${sal}.")

    elif choice==2:
        n=input("Name: ")
        a=input("Age: ")
        eid=input("Employee ID: ")
        sal=float(input("Salary: $"))
        dep=input("Department: ")
        employees.append(Manager(n, a, eid, sal, dep))
        print(f"Manager created with Name:{n}, Age:{a}, Employee ID:{eid}, Salary:${sal}, Department:{dep}.")

    elif choice==3:
        n=input("Name: ")
        a=input("Age: ")
        eid=input("Employee ID: ")
        sal=float(input("Salary: $"))
        lan=input("Programming Language: ")
        employees.append(Developer(n, a, eid, sal, lan))
        print(f"Developer created Name:{n}, Age:{a}, Employee ID:{eid}, Salary:${sal}, Programming language:{lan}.")

    elif choice==4:
        if not employees:
            print("No data found")
            continue
        print("Show Details of:\n 1. Employee\n 2. Manager\n 3. Developer")
        ch=int(input("Enter your choice:"))

        for o  in reversed(employees):
            if ch==1 and type(o) is Employee:
                print("\nEmployee details:")
                o.display()
                break
            elif ch==2 and isinstance(o, Manager):
                print("\nManager details:")
                o.display()
                break
            elif ch==3 and isinstance(o, Developer):
                print("\nDeveloper details:")
                o.display()
                break

    elif choice==5:
        print("Exiting the program. Thank you!")
        break

    else:
        print("Invalid choice. Please choose again!")
