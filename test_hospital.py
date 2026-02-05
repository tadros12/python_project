"""
Test file for Hospital Management System
Tests all 5 classes: Hospital, Person, Department, Patient, and Staff
"""

from hospital import Hospital, Person, Department, Patient, Staff


def test_hospital():
    """Test Hospital class"""
    hospital = Hospital("City Hospital", "123 Main St")
    assert hospital.name == "City Hospital"
    assert hospital.location == "123 Main St"
    assert len(hospital.departments) == 0
    
    # Test add_department method
    dept = Department("Emergency")
    hospital.add_department(dept)
    assert len(hospital.departments) == 1
    assert hospital.departments[0].name == "Emergency"
    print("✓ Hospital class tests passed")


def test_person():
    """Test Person class"""
    person = Person("John Doe", 30)
    assert person.name == "John Doe"
    assert person.age == 30
    
    # Test view_info method
    info = person.view_info()
    assert "John Doe" in info
    assert "30" in info
    print("✓ Person class tests passed")


def test_department():
    """Test Department class"""
    dept = Department("Cardiology")
    assert dept.name == "Cardiology"
    assert len(dept.patients) == 0
    assert len(dept.staff) == 0
    
    # Test add_patient method
    patient = Patient("Jane Smith", 45, "High blood pressure")
    dept.add_patient(patient)
    assert len(dept.patients) == 1
    
    # Test add_staff method
    staff = Staff("Dr. Brown", 40, "Cardiologist")
    dept.add_staff(staff)
    assert len(dept.staff) == 1
    print("✓ Department class tests passed")


def test_patient():
    """Test Patient class"""
    patient = Patient("Alice Johnson", 28, "Broken arm")
    assert patient.name == "Alice Johnson"
    assert patient.age == 28
    assert patient.medical_record == "Broken arm"
    
    # Test view_record method
    record = patient.view_record()
    assert "Alice Johnson" in record
    assert "28" in record
    assert "Broken arm" in record
    
    # Test that Patient inherits from Person
    assert isinstance(patient, Person)
    print("✓ Patient class tests passed")


def test_staff():
    """Test Staff class"""
    staff = Staff("Dr. Smith", 35, "Surgeon")
    assert staff.name == "Dr. Smith"
    assert staff.age == 35
    assert staff.position == "Surgeon"
    
    # Test view_info method
    info = staff.view_info()
    assert "Dr. Smith" in info
    assert "35" in info
    assert "Surgeon" in info
    
    # Test that Staff inherits from Person
    assert isinstance(staff, Person)
    print("✓ Staff class tests passed")


def test_complete_system():
    """Test the complete hospital system integration"""
    # Create a hospital
    hospital = Hospital("General Hospital", "456 Oak Avenue")
    
    # Create departments
    emergency = Department("Emergency")
    surgery = Department("Surgery")
    
    # Add departments to hospital
    hospital.add_department(emergency)
    hospital.add_department(surgery)
    
    # Create patients
    patient1 = Patient("Bob Wilson", 50, "Heart attack")
    patient2 = Patient("Mary Jones", 32, "Appendicitis")
    
    # Add patients to departments
    emergency.add_patient(patient1)
    surgery.add_patient(patient2)
    
    # Create staff
    doctor = Staff("Dr. Williams", 45, "Emergency Physician")
    nurse = Staff("Nurse Johnson", 30, "Head Nurse")
    
    # Add staff to departments
    emergency.add_staff(doctor)
    emergency.add_staff(nurse)
    
    # Verify the complete system
    assert len(hospital.departments) == 2
    assert len(emergency.patients) == 1
    assert len(surgery.patients) == 1
    assert len(emergency.staff) == 2
    
    print("✓ Complete system integration tests passed")


if __name__ == "__main__":
    test_hospital()
    test_person()
    test_department()
    test_patient()
    test_staff()
    test_complete_system()
    print("\n✅ All tests passed successfully!")
