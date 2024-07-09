import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Global tax slabs used for calculating tax
tax_slabs = {
    "Below 60": [[250000, 0.], [500000, 5.], [1000000, 10.], [-1, 15.]],
    "60 or above 60": [[300000, 0.], [500000, 5.], [1000000, 10.], [-1, 15.]],
    "80 or above 80": [[500000, 0.], [1000000, 5.], [-1, 10.]]
}

# Additional deductions under various sections
deductions = {
    "80C": 0,
    "80CCD(1B)": 0,
    "80D": 0,
    "80G": 0,
    "80E": 0,
    "80TTA/TTB": 0
}

def calculate_tax(income, age_category, deductions):
    total_tax_amount = 0.
    tax_slab = tax_slabs[age_category]

    # Calculate tax on income
    for tax_amount, tax_pcnt in tax_slab:
        taxable_amount_slab = income

        if tax_amount == -1:
            income = 0.
        elif income > tax_amount:
            income -= tax_amount
            taxable_amount_slab = tax_amount
        else:
            income = 0.

        if taxable_amount_slab > 0.:
            taxed_amount = ((taxable_amount_slab * tax_pcnt) / 100.0)
            total_tax_amount += taxed_amount

    # Apply deductions
    for section, amount in deductions.items():
        total_tax_amount -= amount

    return total_tax_amount

def predict_future_tax(income, age_category, deductions, years=10):
    prediction = []
    growth_rate = 0.05  # Assume a 5% annual increase in income for prediction

    for year in range(1, years + 1):
        future_income = income * (1 + growth_rate) ** year
        future_tax = calculate_tax(future_income, age_category, deductions)
        prediction.append((year, future_income, future_tax))

    return prediction

def main():
    st.title("Income Tax Calculator with Future Projections")

    # User inputs
    assessment_year = st.text_input("Enter Assessment Year:")
    age_category = st.selectbox("Select Age Category:", ("Below 60", "60 or above 60", "80 or above 80"))
    basic_deductions = st.number_input("Enter Basic Deductions under 80C:", min_value=0.0, step=1000.0)
    nps_contribution = st.number_input("Enter Contribution to NPS under 80CCD(1B):", min_value=0.0, step=1000.0)
    medical_insurance_premium = st.number_input("Enter Medical Insurance Premium under 80D:", min_value=0.0, step=1000.0)
    charity_donation = st.number_input("Enter Donation to Charity under 80G:", min_value=0.0, step=1000.0)
    educational_loan_interest = st.number_input("Enter Interest on Educational Loan under 80E:", min_value=0.0, step=1000.0)
    saving_account_interest = st.number_input("Enter Interest on Deposits in Saving Account under 80TTA/TTB:", min_value=0.0, step=1000.0)
    basic_salary = st.number_input("Enter Basic Salary per annum:", min_value=0.0, step=1000.0)
    da = st.number_input("Enter Dearness Allowance (DA) per annum:", min_value=0.0, step=1000.0)
    hra = st.number_input("Enter HRA per annum:", min_value=0.0, step=1000.0)
    rent_paid = st.number_input("Enter Total Rent Paid per annum:", min_value=0.0, step=1000.0)
    metro_city = st.radio("Do you live in a metro city?", ("Yes", "No"))

    # Convert metro city input to boolean
    if metro_city == "Yes":
        metro_city = True
    else:
        metro_city = False

    # Update deductions dictionary
    deductions["80C"] = basic_deductions
    deductions["80CCD(1B)"] = nps_contribution
    deductions["80D"] = medical_insurance_premium
    deductions["80G"] = charity_donation
    deductions["80E"] = educational_loan_interest
    deductions["80TTA/TTB"] = saving_account_interest

    # Calculate total income
    total_income = basic_salary + da + hra

    # Calculate taxable income
    if hra > rent_paid:
        taxable_income = total_income - rent_paid
    else:
        taxable_income = total_income - hra

    # Calculate tax
    tax_amount = calculate_tax(taxable_income, age_category, deductions)

    # Predict future tax amounts
    future_predictions = predict_future_tax(taxable_income, age_category, deductions)

    # Display result
    st.subheader("Tax Calculation Result:")
    st.write(f"Assessment Year: {assessment_year}")
    st.write(f"Total Income: {total_income}")
    st.write(f"Taxable Income: {taxable_income}")
    st.write(f"Total Tax Amount: {tax_amount}")

    # Display future predictions
    st.subheader("Future Tax Projections:")
    future_years = [str(2024 + year) for year, _, _ in future_predictions]
    future_incomes = [income for _, income, _ in future_predictions]
    future_taxes = [tax for _, _, tax in future_predictions]

    prediction_df = pd.DataFrame({
        "Year": future_years,
        "Projected Income": future_incomes,
        "Projected Tax": future_taxes
    })

    st.dataframe(prediction_df)

    # Plot the future projections
    st.subheader("Future Tax Projections Graph:")
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=future_years, y=future_incomes, marker='^', label="Projected Income", ax=ax)
    sns.lineplot(x=future_years, y=future_taxes, marker='o', label="Projected Tax", ax=ax)
    ax.set_xlabel("Year")
    ax.set_ylabel("Amount (INR)")
    ax.set_title("Projected Income and Tax Over Years")
    ax.legend()
    st.pyplot(fig)

if __name__ == "__main__":
    main()
