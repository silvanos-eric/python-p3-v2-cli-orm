from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()


# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(f"Department {name} not found")


def find_department_by_id():
    # Use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f"Department {id_} not found")


def create_department():
    pass


def update_department():
    pass


def delete_department():
    pass


# You'll implement the employee functions in the lab


def list_employees():
    pass


def find_employee_by_name():
    pass


def find_employee_by_id():
    pass


def create_employee():
    pass


def update_employee():
    pass


def delete_employee():
    pass


def list_department_employees():
    pass
