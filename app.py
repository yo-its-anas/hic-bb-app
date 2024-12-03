# app.py
import streamlit as st
from data import blood_banks
from auth import create_user, authenticate_user

# UI: Home Page
st.title("Karachi Blood Bank Finder")

page = st.sidebar.selectbox("Select Page", ["Find Blood Bank", "Login", "Register"])

if page == "Find Blood Bank":
    st.header("Search for a Blood Bank")
    area = st.selectbox("Select Your Area", [bank["location"] for bank in blood_banks])
    blood_group = st.selectbox("Select Blood Group", ["A+", "B+", "O+", "AB+", "A-", "B-", "O-", "AB-"])
    
    st.write("Nearby Blood Banks:")
    for bank in blood_banks:
        if bank["location"] == area:
            st.markdown(f"""
            **{bank['name']}**  
            Location: {bank['location']}  
            Contact: {bank['contact']}  
            Distance: {bank['distance']} km  
            """)
elif page == "Register":
    st.header("Create an Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    location = st.selectbox("Location", [bank["location"] for bank in blood_banks])
    blood_group = st.selectbox("Preferred Blood Group", ["A+", "B+", "O+", "AB+", "A-", "B-", "O-", "AB-"])
    
    if st.button("Register"):
        st.write(create_user(username, password, email, phone, location, blood_group))
elif page == "Login":
    st.header("Login to Your Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate_user(username, password):
            st.success("Login Successful!")
        else:
            st.error("Invalid credentials.")
