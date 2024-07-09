import streamlit as st

def main():
    st.set_page_config(page_title="Calculator App", page_icon=":moneybag:")

    st.title("Welcome to the Calculator App!")

    st.markdown("""
    Choose from the options below to access different calculators:
    """)

    calculator_choice = st.selectbox("Select Calculator:", ("Tax Calculator", "Financial Calculator", "Income Tax Calculator"))

    if calculator_choice == "Tax Calculator":
        st.subheader("Tax Calculator")
        st.write("Use this calculator to calculate your income tax based on your income and deductions.")
        st.write("Click the button below to access the Tax Calculator.")
        if st.button("Go to Tax Calculator"):
            st.write("Redirecting to Tax Calculator...")
            redirect_url("http://localhost:8502")

    elif calculator_choice == "Financial Calculator":
        st.subheader("Financial Calculator")
        st.write("Use this calculator to perform various financial calculations such as PPF, FD, RD, SIP, etc.")
        st.write("Click the button below to access the Financial Calculator.")
        if st.button("Go to Financial Calculator"):
            st.write("Redirecting to Financial Calculator...")
            redirect_url("http://localhost:8503")

    elif calculator_choice == "Income Tax Calculator":
        st.subheader("Income Tax Calculator")
        st.write("Use this calculator to calculate your income tax based on your income, age, and deductions.")
        st.write("Click the button below to access the Income Tax Calculator.")
        if st.button("Go to Income Tax Calculator"):
            st.write("Redirecting to Income Tax Calculator...")
            redirect_url("http://localhost:8504")

def redirect_url(url):
    # Javascript to open the URL in a new popup window
    js = f"window.open('{url}', '_blank')"
    html = f"<script>{js}</script>"
    st.markdown(html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
