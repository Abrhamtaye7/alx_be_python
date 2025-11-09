# finance_calculator.py

# 1. Ask the user for their monthly financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# 2. Calculate monthly savings
# Formula: savings = income - expenses
monthly_savings = monthly_income - monthly_expenses

# 3. Project the savings over one year with 5% annual interest
# Annual savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# 4. Display the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
