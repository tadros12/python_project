"""
Demo script for Hospital Management System
Demonstrates usage of all 5 classes
"""

from hospital import Hospital, Person, Department, Patient, Staff


def main():
    print("=" * 60)
    print("Hospital Management System Demo")
    print("=" * 60)
    
    # Create a hospital
    hospital = Hospital("City General Hospital", "123 Medical Center Drive")
    print(f"\n🏥 Created Hospital: {hospital.name}")
    print(f"   Location: {hospital.location}")
    
    # Create departments
    print("\n📋 Creating Departments...")
    emergency = Department("Emergency")
    cardiology = Department("Cardiology")
    surgery = Department("Surgery")
    
    # Add departments to hospital
    hospital.add_department(emergency)
    hospital.add_department(cardiology)
    hospital.add_department(surgery)
    print(f"   Added {len(hospital.departments)} departments to the hospital")
    
    # Create patients
    print("\n👤 Creating Patients...")
    patient1 = Patient("John Doe", 45, "Chest pain, suspected heart attack")
    patient2 = Patient("Jane Smith", 32, "Broken leg from car accident")
    patient3 = Patient("Bob Johnson", 67, "Scheduled bypass surgery")
    
    # Display patient records
    print(f"   {patient1.view_record()}")
    print(f"   {patient2.view_record()}")
    print(f"   {patient3.view_record()}")
    
    # Create staff
    print("\n👨‍⚕️ Creating Staff Members...")
    doctor1 = Staff("Dr. Sarah Williams", 42, "Cardiologist")
    doctor2 = Staff("Dr. Michael Chen", 38, "Surgeon")
    nurse1 = Staff("Nurse Emily Davis", 29, "Emergency Nurse")
    nurse2 = Staff("Nurse Tom Brown", 35, "Surgical Nurse")
    
    # Display staff info
    print(f"   {doctor1.view_info()}")
    print(f"   {doctor2.view_info()}")
    print(f"   {nurse1.view_info()}")
    print(f"   {nurse2.view_info()}")
    
    # Assign patients to departments
    print("\n🏥 Assigning Patients to Departments...")
    emergency.add_patient(patient1)
    emergency.add_patient(patient2)
    surgery.add_patient(patient3)
    print(f"   Emergency Department: {len(emergency.patients)} patients")
    print(f"   Surgery Department: {len(surgery.patients)} patients")
    
    # Assign staff to departments
    print("\n👨‍⚕️ Assigning Staff to Departments...")
    emergency.add_staff(nurse1)
    cardiology.add_staff(doctor1)
    surgery.add_staff(doctor2)
    surgery.add_staff(nurse2)
    print(f"   Emergency Department: {len(emergency.staff)} staff members")
    print(f"   Cardiology Department: {len(cardiology.staff)} staff members")
    print(f"   Surgery Department: {len(surgery.staff)} staff members")
    
    # Summary
    print("\n" + "=" * 60)
    print("Hospital Summary")
    print("=" * 60)
    print(f"Hospital: {hospital.name}")
    print(f"Total Departments: {len(hospital.departments)}")
    total_patients = sum(len(dept.patients) for dept in hospital.departments)
    total_staff = sum(len(dept.staff) for dept in hospital.departments)
    print(f"Total Patients: {total_patients}")
    print(f"Total Staff: {total_staff}")
    print("\n✅ Demo completed successfully!")


if __name__ == "__main__":
    main()
