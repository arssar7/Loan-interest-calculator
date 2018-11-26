# user input

principal_amount = float(input("total loan amount: "))
interest_rate = float(input("annual interest rate: "))
duration = int(input("loan duration in years: "))

# amounts per month
def monthly_loan(principal,interest_rate,duration):
    n = duration*12 #total number of months
    r = interest_rate/(100*12) #interest per month
    monthly_payment = principal_amount*((r*((r+1)**n))/(((r+1)**n)-1)) #formula for compound interest applied on mothly payments.
    return monthly_payment

# ---funtion for remaining loan balance calculation---
def remaining_balance(principal_amount,annual_interest_rate,duration,payments):
    r = annual_interest_rate/1200 # monthly interest rate
    m = r + 1
    n = duration*12 # duration in months
    
    # remaining balance using compound interest formula
    remaining = principal_amount*(((m**n)-(m**payments))/((m**n)-1))
    return remaining

monthly = monthly_loan(principal_amount,interest_rate,duration)

print("Loan amount: ",principal_amount," Interest rate: ",interest_rate)

print("Duration (Years): ",duration," Monthly payment: ",int(monthly))

for x in range(1,duration+1):
    mon = x*12
    rem = remaining_balance(principal_amount,interest_rate,duration,mon)

print("Year: ",x," Balance remaining: ",int(rem)," Total payments: ",int(monthly*mon))
