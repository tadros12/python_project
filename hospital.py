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
        self.departments.append(department)


class Person:
    """Person class with name and age attributes"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def view_info(self):
        """View person information"""
        return f"Name: {self.name}, Age: {self.age}"


class Department:
    """Department class with name attribute"""
    
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.staff = []
    
    def add_patient(self, patient):
        """Add a patient to the department"""
        self.patients.append(patient)
    
    def add_staff(self, staff):
        """Add a staff member to the department"""
        self.staff.append(staff)


class Patient(Person):
    """Patient class inheriting from Person with medical_record attribute"""
    
    def __init__(self, name, age, medical_record):
        super().__init__(name, age)
        self.medical_record = medical_record
    
    def view_record(self):
        """View patient's medical record"""
        return f"Patient: {self.name}, Age: {self.age}, Medical Record: {self.medical_record}"


class Staff(Person):
    """Staff class inheriting from Person with position attribute"""
    
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position
    
    def view_info(self):
        """View staff information"""
        return f"Staff - Name: {self.name}, Age: {self.age}, Position: {self.position}"
