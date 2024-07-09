import streamlit as st

# Function to render the navigation menu based on the user's role
def menu():
    if st.session_state.role is None:
        unauthenticated_menu()
    else:
        authenticated_menu()

# Render the menu for unauthenticated users
def unauthenticated_menu():
    st.sidebar.markdown("[Log in](app.py)")

# Render the menu for authenticated users
def authenticated_menu():
    st.sidebar.markdown("[Switch accounts](app.py)")
    st.sidebar.markdown("[Tax Calculator](pages/tax_calculator.py)")
    st.sidebar.markdown("[Financial Calculator](pages/financial_calculator.py)")
    st.sidebar.markdown("[Income Tax Calculator](pages/incometax_calculator.py)")
