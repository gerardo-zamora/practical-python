# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
current_payment = payment
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month = month + 1

    if (month >= extra_payment_start_month) and (month <= extra_payment_end_month):
        current_payment = payment + extra_payment
    else:
        current_payment = payment

    if (principal < current_payment):
        total_paid = total_paid + principal
        principal = 0
    else:    
        total_paid = total_paid + current_payment
        principal = principal * (1+rate/12) - current_payment

    print(f'{month:0d}, ${total_paid:0.2f}, ${principal:0.2f}')


print(f'Total paid: ${total_paid:0.2f}, Months: {month}')