import streamlit as st
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

# # Download NLTK data
# nltk.download('vader_lexicon')

# # Initialize the sentiment analyzer
# sid = SentimentIntensityAnalyzer()
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    return sentiment_score

def calculate_ppf(principal, annual_interest_rate, years):
    total = principal * ((1 + annual_interest_rate / 100) ** years)
    return total

def calculate_epf(monthly_contribution, annual_interest_rate, years):
    total = monthly_contribution * 12 * ((1 + annual_interest_rate / 100) ** years)
    return total

def calculate_fd(principal, annual_interest_rate, years):
    total = principal * ((1 + annual_interest_rate / 100) ** years)
    return total

def calculate_rd(monthly_contribution, annual_interest_rate, years):
    total = monthly_contribution * 12 * years * (years + 1) / 2 + monthly_contribution * 12 * years * annual_interest_rate / 100 * (years + 1) / 2
    return total

def calculate_sip(monthly_investment, annual_interest_rate, years):
    total = monthly_investment * 12 * years * ((1 + annual_interest_rate / 100) ** years - 1) / (annual_interest_rate / 100)
    return total

def calculate_mutual_fund(principal, annual_interest_rate, years):
    total = principal * ((1 + annual_interest_rate / 100) ** years)
    return total

def calculate_emi(loan_amount, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    emi = loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** (years * 12)) / (((1 + monthly_interest_rate) ** (years * 12)) - 1)
    return emi


def main():
    st.title("Financial Calculator with AI Integration")

    calculator = st.selectbox("Select Calculator:", ("PPF", "EPF", "FD", "RD", "SIP", "Mutual Fund", "EMI", "Personalized Recommendations"))

    if calculator == "PPF":
        st.subheader("Public Provident Fund (PPF) Calculator")
        principal = st.number_input("Enter Principal Amount:", min_value=0.0, step=1000.0)
        annual_interest_rate = st.number_input("Enter Annual Interest Rate (%):", min_value=0.0, step=0.1)
        years = st.number_input("Enter Number of Years:", min_value=0, step=1)
        if st.button("Calculate"):
            total_amount = calculate_ppf(principal, annual_interest_rate, years)
            st.write(f"Total Amount after {years} years: {total_amount:.2f}")

    elif calculator == "EPF":
        st.subheader("Employee Provident Fund (EPF) Calculator")
        monthly_contribution = st.number_input("Enter Monthly Contribution:", min_value=0.0, step=100.0)
        annual_interest_rate = st.number_input("Enter Annual Interest Rate (%):", min_value=0.0, step=0.1)
        years = st.number_input("Enter Number of Years:", min_value=0, step=1)
        if st.button("Calculate"):
            total_amount = calculate_epf(monthly_contribution, annual_interest_rate, years)
            st.write(f"Total Amount after {years} years: {total_amount:.2f}")

    elif calculator == "FD":
        st.subheader("Fixed Deposit (FD) Calculator")
        principal = st.number_input("Enter Principal Amount:", min_value=0.0, step=1000.0)
        annual_interest_rate = st.number_input("Enter Annual Interest Rate (%):", min_value=0.0, step=0.1)
        years = st.number_input("Enter Number of Years:", min_value=0, step=1)
        if st.button("Calculate"):
            total_amount = calculate_fd(principal, annual_interest_rate, years)
            st.write(f"Total Amount after {years} years: {total_amount:.2f}")

    elif calculator == "RD":
        st.subheader("Recurring Deposit (RD) Calculator")
        monthly_contribution = st.number_input("Enter Monthly Contribution:", min_value=0.0, step=100.0)
        annual_interest_rate = st.number_input("Enter Annual Interest Rate (%):", min_value=0.0, step=0.1)
        years = st.number_input("Enter Number of Years:", min_value=0, step=1)
        if st.button("Calculate"):
            total_amount = calculate_rd(monthly_contribution, annual_interest_rate, years)
            st.write(f"Total Amount after {years} years: {total_amount:.2f}")

    elif calculator == "SIP":
        st.subheader("Systematic Investment Plan (SIP) Calculator")
        monthly_investment = st.number_input("Enter Monthly Investment:", min_value=0.0, step=100.0)
        annual_interest_rate = st.number_input("Enter Annual Interest Rate (%):", min_value=0.0, step=0.1)
        years = st.number_input("Enter Number of Years:", min_value=0, step=1)
        if st.button("Calculate"):
            total_amount = calculate_sip(monthly_investment, annual_interest_rate, years)
            st.write(f"Total Amount after {years} years: {total_amount:.2f}")

    elif calculator == "Mutual Fund":
        st.subheader("Mutual Fund Return Calculator")
        principal = st.number_input("Enter Principal Amount:", min_value=0.0, step=1000.0)
        annual_interest_rate = st.number_input("Enter Annual Interest Rate (%):", min_value=0.0, step=0.1)
        years = st.number_input("Enter Number of Years:", min_value=0, step=1)
        if st.button("Calculate"):
            total_amount = calculate_mutual_fund(principal, annual_interest_rate, years)
            st.write(f"Total Amount after {years} years: {total_amount:.2f}")

    elif calculator == "EMI":
        st.subheader("Equated Monthly Installment (EMI) Calculator")
        loan_amount = st.number_input("Enter Loan Amount:", min_value=0.0, step=1000.0)
        annual_interest_rate = st.number_input("Enter Annual Interest Rate (%):", min_value=0.0, step=0.1)
        years = st.number_input("Enter Number of Years:", min_value=0, step=1)
        if st.button("Calculate"):
            emi = calculate_emi(loan_amount, annual_interest_rate, years)
            st.write(f"Monthly EMI: {emi:.2f}")

    elif calculator == "Personalized Recommendations":
        st.subheader("Personalized Recommendations")

       # User input for text analysis
        text = st.text_area("Enter the text to analyze:")

        if st.button("Analyze Text"):
            sentiment_score = analyze_sentiment(text)
            st.write(f"Sentiment Score: {sentiment_score}")

            # Provide personalized recommendation based on sentiment score
            if sentiment_score >= 0.5:
                st.write("You seem to have a positive sentiment. Consider investing in growth-oriented assets.")
            elif sentiment_score <= -0.5:
                st.write("You seem to have a negative sentiment. Consider investing in safer assets or seek financial advice.")
            else:
                st.write("Your sentiment is neutral. You may consider a balanced approach to investments.")

if __name__ == "__main__":
    main()
# #from menu import menu_with_redirect

# # Render the navigation menu with redirect
# #menu_with_redirect()

# def calculate_ppf(principal, annual_interest_rate, years):
#     total = principal * ((1 + annual_interest_rate / 100) ** years)
#     return total


# def main():
#     st.title("Financial Calculator")

#     calculator = st.selectbox("Select Calculator:", ("PPF", "EPF", "FD", "RD", "SIP", "Mutual Fund", "EMI"))

#     if calculator == "PPF":
#         st.subheader("Public Provident Fund (PPF) Calculator")
#         principal = st.number_input("Enter Principal Amount:", min_value=0.0, step=1000.0)
#         annual_interest_rate = st.number_input("Enter Annual Interest Rate (%):", min_value=0.0, step=0.1)
#         years = st.number_input("Enter Number of Years:", min_value=0, step=1)
#         if st.button("Calculate"):
#             total_amount = calculate_ppf(principal, annual_interest_rate, years)
#             st.write(f"Total Amount after {years} years: {total_amount:.2f}")

    

# if __name__ == "__main__":
#     main()
