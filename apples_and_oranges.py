print("The price of Apple is 20 pesos")
print("The price of Orange is 25 pesos")

def value_of_apple():
    apple = 20 
    return apple

def value_of_oranges():
    oranges = 25 
    return oranges

def quantity_of_apples_to_buy():
    quantity_of_apples = int(input("How many apples you want to buy? "))
    return quantity_of_apples

def quantity_of_oranges_to_buy():
    quantityoforanges = int(input("How many oranges you want to buy? "))
    return quantityoforanges

def total_of_fruits(amount_of_appleF,  number_of_applesF, amount_of_orangesF, number_of_orangesF):
    totalofapples= (amount_of_appleF * number_of_applesF) + (amount_of_orangesF * number_of_orangesF)
    return totalofapples
     
def total_amount_of_fruits(total_payF):
    print(f"The total amount is {total_payF}")

amount_of_apple= value_of_apple()

amount_of_oranges= value_of_oranges()

number_of_apples = quantity_of_apples_to_buy()

number_of_oranges = quantity_of_oranges_to_buy()

total_pay= total_of_fruits(amount_of_apple, number_of_apples, amount_of_oranges, number_of_oranges)

total_amount_of_fruits(total_pay)



