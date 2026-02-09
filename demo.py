import streamlit as st
from hospital import Staff, Patient, Department

# Initialize "Database" in Session State so data persists during clicks
if 'departments' not in st.session_state:
    st.session_state.departments = {
        "Emergency": Department("Emergency"),
        "Cardiology": Department("Cardiology")
    }

st.set_page_config(page_title="Hospital MS", layout="wide")
st.title("🏥 Hospital Management System")

# Sidebar for Navigation
menu = st.sidebar.selectbox("Navigation", ["Dashboard", "Add Staff", "Register Patient"])

if menu == "Dashboard":
    st.header("Hospital Overview")
    cols = st.columns(len(st.session_state.departments))
    
    for i, (name, dept) in enumerate(st.session_state.departments.items()):
        with cols[i]:
            st.subheader(f"Unit: {name}")
            st.metric("Staff", len(dept.staff_list))
            st.metric("Patients", len(dept.patient_list))
            
            if st.button(f"View Details: {name}"):
                st.write("**Staff members:**", [s.name for s in dept.staff_list])
                st.write("**Patients:**", [p.name for p in dept.patient_list])


# elif menu == "Add Staff":
#     st.header("Register New Staff Member")
#     with st.form("staff_form"):
#         name = st.text_input("Full Name")
#         age = st.number_input("Age", min_value=18, max_value=100)
#         gender = st.selectbox("Gender", ["Male", "Female", "Other"])
#         role = st.text_input("Role (e.g. Surgeon, Nurse)")
#         salary = st.number_input("Monthly Salary", min_value=0)
#         dept_name = st.selectbox("Department", list(st.session_state.departments.keys()))
        
#         submitted = st.form_submit_button("Hire Staff")
#         if submitted:
#             new_staff = Staff(name, age, gender, "N/A", role, salary)
#             st.session_state.departments[dept_name].staff_list.append(new_staff)
#             st.success(f"Added {name} to {dept_name}")


elif menu == "Register Patient":
    st.header("In-patient Admission")
    with st.form("patient_form"):
        name = st.text_input("Patient Name")
        age = st.number_input("Age", min_value=0, max_value=120)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        record = st.text_area("Medical Condition / Reason for Visit")
        dept_name = st.selectbox("Assign to Department", list(st.session_state.departments.keys()))
        
        submitted = st.form_submit_button("Admit Patient")
        if submitted:
            new_patient = Patient(name, age, gender, "N/A", record)
            st.session_state.departments[dept_name].patient_list.append(new_patient)
            st.info(f"Patient {name} admitted to {dept_name}")