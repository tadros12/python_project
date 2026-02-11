import streamlit as st
from hospital import Staff, Patient, Department

# Reset button to fix state issues during development
if st.sidebar.button("System Reset (Clear All Data)"):
    st.session_state.clear()
    st.rerun()

if 'departments' not in st.session_state:
    st.session_state.departments = {
        "Emergency": Department("Emergency"),
        "Cardiology": Department("Cardiology")
    }

st.title("🏥 Hospital Management System")

menu = st.sidebar.selectbox("Navigation", ["Dashboard", "Staff Management", "Patient Admission"])

        ## main dashboard with hospital overview ##
if menu == "Dashboard":
    st.header("Hospital Overview")
    cols = st.columns(len(st.session_state.departments))
    
    for i, (name, dept) in enumerate(st.session_state.departments.items()):
        with cols[i]:
            st.subheader(f"Unit: {name}")
            st.metric("Staff", len(dept.staff_list))
            st.metric("Patients", len(dept.patients_list))
            
            with st.expander(f"View {name} Lists"):
                st.write("**Doctors/Nurses:**")
                for s in dept.staff_list: st.text(f"• {s.name} ({s.role})")
                st.write("**Patients:**")
                for p in dept.patients_list: st.text(f"• {p.name} (ID: {p.medical_record_id})")



        ##staff management##
elif menu == "Staff Management":
    st.header("Register New Staff")
    with st.form("staff_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", 18, 100, 30)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        role = st.text_input("Role")
        salary = st.number_input("Salary", min_value=0)
        dept_name = st.selectbox("Assign to", list(st.session_state.departments.keys()))
        
        if st.form_submit_button("Hire Staff"):
            new_staff = Staff(name, age, gender, "Contact N/A", role, salary)
            st.session_state.departments[dept_name].add_staff(new_staff)
            st.success(f"Staff {name} hired!")



        ##patient admission##
elif menu == "Patient Admission":
    st.header("Patient Intake")
    with st.form("patient_form"):
        name = st.text_input("Patient Name")
        age = st.number_input("Age", 0, 120, 25)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        rec_id = st.text_input("Medical Record")
        dept_name = st.selectbox("Department", list(st.session_state.departments.keys()))
        
        if st.form_submit_button("Admit Patient"):
            new_patient = Patient(name, age, gender, "Contact N/A", rec_id)
            st.session_state.departments[dept_name].add_patient(new_patient)
            st.success(f"Patient {name} admitted to {dept_name}")