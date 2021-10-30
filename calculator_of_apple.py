def cash():
    money_of_user= int(input("Amount of Money you have?: "))
    return money_of_user

def price_of_apple():
    amount_of_apple= int(input("How much does an apple cost?: "))
    return amount_of_apple

def capacity_to_buy(cashF, Apple_priceF):
    user_can_buy= cashF//Apple_priceF
    return user_can_buy

def change_of_user(cashF, Apple_priceF):
    user_change= cashF%Apple_priceF
    return user_change

def capacity_and_change(User_can_buyF, Change_of_userF):
    print(f"You can buy {User_can_buyF} apples and your change is {Change_of_userF} pesos.")

moneyUser= cash()
appleUser= price_of_apple()
User_can_buy=capacity_to_buy(moneyUser, appleUser)
Change_of_user= change_of_user(moneyUser, appleUser)
capacity_and_change(User_can_buy, Change_of_user)