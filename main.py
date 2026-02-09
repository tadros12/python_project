import streamlit as st
from hospital import Staff, Patient, Department

# clean start to clear old "Department" objects
if st.sidebar.button("Clean Reset (Fix AttributeErrors)"):
    st.session_state.clear()
    st.rerun()

if 'departments' not in st.session_state:
    st.session_state.departments = {
        "Emergency": Department("Emergency"),
        "Cardiology": Department("Cardiology")
    }

st.title("🏥 Hospital MS - Staff Testing Mode")

menu = st.sidebar.selectbox("Navigation", ["Dashboard", "Add Staff"])

if menu == "Dashboard":
    st.header("Staffing Overview")
    cols = st.columns(len(st.session_state.departments))
    
    for i, (name, dept) in enumerate(st.session_state.departments.items()):
        with cols[i]:
            st.subheader(f"Unit: {name}")
            # Only testing Staff for now
            st.metric("Staff Count", len(dept.staff_list))
            
            if st.button(f"View Staff: {name}"):
                if dept.staff_list:
                    for s in dept.staff_list:
                        st.write(f"**{s.name}** ({s.role})")
                else:
                    st.write("No staff assigned.")

elif menu == "Add Staff":
    st.header("Register New Staff Member")
    with st.form("staff_form"):
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        role = st.text_input("Role (e.g. Surgeon, Nurse)")
        salary = st.number_input("Monthly Salary", min_value=0, value=5000)
        dept_name = st.selectbox("Department", list(st.session_state.departments.keys()))
        
        submitted = st.form_submit_button("Hire Staff")
        if submitted:
            # Note: Ensure your Staff class __init__ matches these 6 arguments!
            new_staff = Staff(name, age, gender, "Contact N/A", role, salary)
            st.session_state.departments[dept_name].staff_list.append(new_staff)
            st.success(f"Added {name} to {dept_name}")