#python

Child_meal = float(input("What is the price of a child's meal?"))
Adult_meal = float(input("What is the price of an adult's meal?"))
Number_of_children = int(input('How many children are there?'))
Number_of_adults = int(input('How many adults are there?'))
Tax_rate = float(input('What is the sales tax rate?'))
Tip_rate = int(input('What is the percentage of tip?'))

Subtotal = Child_meal * Number_of_children + Adult_meal * Number_of_adults
Sales_tax = Subtotal % Tax_rate 
Total = Subtotal + Sales_tax
Tip = Total % Tip_rate

print(f'''
Subtotal: ${round(Subtotal,2)}
Sales Tax: ${round(Sales_tax,2)}
Total: ${round(Total,2)}
Tip: ${round(Tip,2)}
''')

payment_amount = float(input("What is the payment amount?"))
Change = payment_amount - Total - Tip
print(f'Change: ${Change}')

#What is the price of a child's meal? 2.25
#What is the price of an adult's meal? 6.99
#How many children are there? 2
#How many adults are there? 1
#What is the sales tax rate? 4

#Subtotal: $11.49
#Sales Tax: $0.46
#Total: $11.95

#What is the payment amount? 20
#Change: $8.05