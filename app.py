# app.py

import streamlit as st
from bank import bank  # Import the bank instance

st.title("🏦 Bank Management System")

# Navigation for different operations
menu = ["Create Account", "Deposit", "Withdraw", "View Account"]
choice = st.sidebar.selectbox("Select an option", menu)

# Store account details in session state
if "account_number" not in st.session_state:
    st.session_state.account_number = None

# Create Account
if choice == "Create Account":
    st.subheader("🔹 Create a New Bank Account")
    name = st.text_input("Enter Your Name")
    initial_balance = st.number_input("Enter Initial Deposit (₹)", min_value=0, step=100)

    if st.button("Create Account"):
        if name and initial_balance >= 0:
            acc_num = bank.create_account(name, initial_balance)
            st.session_state.account_number = acc_num  # Store account number in session
            st.success(f"Account created successfully! Your Account Number: {acc_num}")
        else:
            st.error("Please enter valid details.")

# Deposit Money
elif choice == "Deposit":
    st.subheader("🔹 Deposit Money")
    acc_num = st.number_input("Enter Account Number", min_value=1, step=1)
    amount = st.number_input("Enter Deposit Amount (₹)", min_value=0, step=100)

    if st.button("Deposit"):
        msg = bank.deposit(acc_num, amount)
        st.success(msg)

# Withdraw Money
elif choice == "Withdraw":
    st.subheader("🔹 Withdraw Money")
    acc_num = st.number_input("Enter Account Number", min_value=1, step=1)
    amount = st.number_input("Enter Withdrawal Amount (₹)", min_value=0, step=100)

    if st.button("Withdraw"):
        msg = bank.withdraw(acc_num, amount)
        if "successfully" in msg:
            st.success(msg)
        else:
            st.error(msg)

# View Account Details
elif choice == "View Account":
    st.subheader("🔹 View Account Details")
    acc_num = st.number_input("Enter Account Number", min_value=1, step=1)

    if st.button("View Details"):
        details = bank.get_account_details(acc_num)
        if isinstance(details, dict):
            st.json(details)  # Display details in JSON format
        else:
            st.error(details)
