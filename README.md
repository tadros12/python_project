# Hospital Management System

A Python-based hospital management system with 5 classes for managing hospitals, departments, patients, and staff.

## Features

### Classes

1. **Hospital** - Manages hospital information and departments
   - Attributes: `name`, `location`
   - Methods: `add_department()`

2. **Person** - Base class for Patient and Staff
   - Attributes: `name`, `age`
   - Methods: `view_info()`

3. **Department** - Manages department information
   - Attributes: `name`
   - Methods: `add_patient()`, `add_staff()`

4. **Patient** - Represents a patient (inherits from Person)
   - Attributes: `name`, `age`, `medical_record`
   - Methods: `view_record()`

5. **Staff** - Represents a staff member (inherits from Person)
   - Attributes: `name`, `age`, `position`
   - Methods: `view_info()`

## Usage

### Basic Example

```python
from hospital import Hospital, Department, Patient, Staff

# Create a hospital
hospital = Hospital("City Hospital", "123 Main St")

# Create a department
emergency = Department("Emergency")
hospital.add_department(emergency)

# Create a patient
patient = Patient("John Doe", 45, "Chest pain")
emergency.add_patient(patient)

# Create a staff member
doctor = Staff("Dr. Smith", 38, "Emergency Physician")
emergency.add_staff(doctor)

# View information
print(patient.view_record())
print(doctor.view_info())
```

## Running the Code

### Run Tests
```bash
python test_hospital.py
```

### Run Demo
```bash
python demo.py
```

## Files

- `hospital.py` - Main module with all 5 classes
- `test_hospital.py` - Comprehensive test suite
- `demo.py` - Demonstration script showing system usage

## Security Summary

✅ CodeQL security scan completed with no vulnerabilities found.