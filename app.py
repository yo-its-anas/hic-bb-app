import streamlit as st
from auth import create_user, login_user
from data import get_blood_banks

# UI Enhancement with CSS
st.markdown("""
    <style>
        .stButton > button {
            background-color: #ff5733;
            color: white;
            border-radius: 8px;
        }
        .blood-bank-box {
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 10px;
            margin-bottom: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

st.title("Karachi Blood Bank Finder")

# Tabs for User Login & Blood Bank Finder
tab1, tab2 = st.tabs(["Find Blood Bank", "User Account"])

with tab1:
    st.header("Find Nearby Blood Bank")
    location = st.selectbox("Select Your Location:", [
        "Clifton", "Saddar", "Gulshan-e-Iqbal", "DHA", "Nazimabad", "Korangi", 
        "Liaquatabad", "Malir", "Landhi", "Orangi Town", "Shah Faisal Colony",
        "PECHS", "Gulistan-e-Jauhar"
    ])
    blood_group = st.selectbox("Select Required Blood Group:", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
    
    if st.button("Find Blood Banks"):
        blood_banks = get_blood_banks(location, blood_group)
        if blood_banks:
            for bank in blood_banks:
                st.markdown(f"""
                <div class='blood-bank-box'>
                    <strong>Name:</strong> {bank['name']}<br>
                    <strong>Location:</strong> {bank['location']}<br>
                    <strong>Contact:</strong> {bank['contact']}<br>
                    <strong>Distance:</strong> {bank['distance']} km
                </div>
                """, unsafe_allow_html=True)
        else:
            st.error("No blood banks found nearby.")

with tab2:
    st.subheader("User Account")
    action = st.radio("Choose Action", ["Login", "Register"])
    
    if action == "Register":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        location = st.selectbox("Location:", ["Clifton", "Saddar", "Nazimabad", "Malir"])
        blood_group = st.selectbox("Preferred Blood Group:", ["A+", "O+", "B+", "AB+"])
        if st.button("Register"):
            st.write(create_user(username, password, email, phone, location, blood_group))
    
    elif action == "Login":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            result = login_user(username, password)
            if result:
                st.success("Login successful!")
            else:
                st.error("Invalid credentials.")
