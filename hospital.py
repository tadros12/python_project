"""
Hospital Management System
Contains classes for Hospital, Person, Department, Patient, and Staff
"""


class Hospital:
    """Hospital class with name and location attributes"""
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []
    
    def add_department(self, department):
        """Add a department to the hospital"""
        if not isinstance(department, Department):
            raise TypeError("Expected Department instance")
        self.departments.append(department)


class Person:
    """Person class with name and age attributes
    param name: str - person's name
    param age: int - person's age (must be non-negative)
    """
    
    def __init__(self, name, age , gender , contact_info):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_info = contact_info
    
    def set_age(self, age):
        """Set person's age with validation
            param age: int - age must be non-negative
        """
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.age = age
        
        
        
    def view_info(self):
        """View person information"""
        return f"Name: {self.name}, Age: {self.age}"


class Department:
    """Department class with name attribute"""
    
    def __init__(self, name):
        self.name = name
        self.patients_list = []
        self.staff_list = []
    
    def add_patient(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("Expected Patient instance")
        self.patients_list.append(patient)
    
    def add_staff(self, staff):
        if not isinstance(staff, Staff):
            raise TypeError("Expected Staff instance")
        self.staff_list.append(staff)


class Patient(Person):
    """Simple Patient class"""

    def __init__(self, name, age, gender, contact_info, medical_record_id):
        super().__init__(name, age, gender, contact_info)
        self.medical_record_id = medical_record_id

        self.medications = []    
        self.visits = []
        self.doctor_notes = []
            
    def add_medication(self, medication):
        self.medications.append(medication)

    def add_visit(self, date, reason):
        self.visits.append(f"{date} - {reason}")

    def add_doctor_note(self, note):
        self.doctor_notes.append(note)

    def view_record(self):
        return f"""
Patient Name: {self.name}
Age: {self.age}
Medical Record ID: {self.medical_record_id}

Medications:
{self.medications}

Visits:
{self.visits}

Doctor Notes:
{self.doctor_notes}
"""

class Staff(Person):

    """ 
    staff class inheriting from Person with role and salary attributes
    param role: str - staff role 
    param salary: float - staff salary 
    
    """
    
    def __init__(self, name, age, gender, contact_info, role, salary):
        super().__init__(name, age, gender, contact_info)
        self.role = role
        self.__salary = salary  #private
        self.is_active = True

    def get_salary(self):

        return f"${self.__salary:,.2f}"
    

    def update_salary(self, amount):
        """ 
        Update staff salary with validation
        param amount: float - new salary amount


        """
        if amount > 0:
            self.__salary = amount
            print(f"Salary updated for {self.name}.")
        else:
            print("Invalid salary amount.")

    def view_info(self):
        status = "Active" if self.is_active else "On Leave/Retired"
        return f"Staff: {self.name} | Role: {self.role} | Status: {status}"
    