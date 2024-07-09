import streamlit as st

def main():
    st.set_page_config(page_title="Calculator App", layout="wide")

    st.title("Welcome to the Calculator App!")

    

    # st.sidebar.title("Navigation")

    # # Navigation links to different calculators
    # if st.sidebar.button("Tax Calculator"):
    #     st.markdown("[Tax Calculator](http://localhost:8501)")
    # if st.sidebar.button("Financial Calculator"):
    #     st.markdown("[Financial Calculator](http://localhost:8502)")
    # if st.sidebar.button("Income Tax Calculator"):
    #     st.markdown("[Income Tax Calculator](http://localhost:8503)")

if __name__ == "__main__":
    main()
