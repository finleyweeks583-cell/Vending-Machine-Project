import time
paid = False
valid_letter = False

CEREAL_BAR = 0.50
CRISPS = 0.60
CHOCOLATE_BAR = 0.80
BOTTLED_WATER = 0.90

print("=========   Options   =========")
print("Cereal Bar     :        £0.50  ")
print("Crisps         :        £0.60  ")
print("Chocolate Bar  :        £0.80  ")
print("Bottled Water  :        £0.90  ")
print("===============================")

print()

print("Press 'A' for Cereal Bar   ")
print("Press 'B' for Crisps       ")
print("Press 'C' for Chocolate Bar")
print("Press 'D' for Bottled Water")

print()

while (not valid_letter):            # Takes in the users choice of what item they want to buy, sets the variables 'item' and 'price' to the values of a item depending on the letter a user inputs
    letter = input("Please input letter: ").strip().upper()
    print()

    if letter == "A":
        item = "Cereal Bar"
        price = CEREAL_BAR
        valid_letter = True

    elif letter == "B":
        item = "Crisps"
        price = CRISPS
        valid_letter = True

    elif letter == "C":
        item = "Chocolate Bar"
        price = CHOCOLATE_BAR
        valid_letter = True

    elif letter == "D":
        item = "Bottled Water"
        price = BOTTLED_WATER
        valid_letter = True

    else:
        time.sleep(1)
        print("That is not a valid letter, please try again!")    
        print()
        valid_letter = False        # will loop the code from line 26 if the user inputs a invalid letter allowing them to chose the right item


coins = []
VALID_COINS = [0.10, 0.20, 0.50, 1.00]

while True:
    while (not paid):            # Takes in the users coins, adds them up and keeps a total as well as only accepting the valid coins (10p, 20p, 50p and £1)    
        time.sleep(1)
        coin_input = input("Input Coins, press 'Enter' when done: £")
        print()

        if coin_input == "":
            break
        coin = float(coin_input)

        if coin in VALID_COINS:
            coins.append(coin)
            print(f"Your total funds so far: £{sum(coins):.2f}")
            print()
        else:
            time.sleep(1.5)
            print()
            print("Coins not accepted, Please input only 10p, 20p, 50p and £1 coins")     # will loop the code from the start of line 61 if a user inputs a invalid coin   
            print()

    total = sum(coins)

    if total == price:           # accepts the payment and outputs the item if the user has entered total of coins equal to the item they chose 
        print("Authorising....")
        print()
        time.sleep(1)
        print("Authorising...")
        print()
        time.sleep(1)
        print("Authorising..")
        print()
        time.sleep(3)
        print("Payment accepted!")
        print()
        time.sleep(1.5)
        print(f"Here is your {item}, Thank you for your purchase!")
        print()
        paid = True
        break

    elif total < price:            # loops the code to input coins if the user has put in less than total needed to buy their chosen item
        print("Authorising....")
        print()
        time.sleep(1)
        print("Authorising...")
        print()
        time.sleep(1)
        print("Authorising..")
        print()
        time.sleep(3)
        print("Insufficent funds, please try again")
        print()
        paid = False

    elif total > price:              # calculates change if the user has input more coins then needed for their chosen item, also outputs the chosen item and change
        change = total - price
        print("Authorising....")
        print()
        time.sleep(1)
        print("Authorising...")
        print()
        time.sleep(1)
        print("Authorising..")
        print()
        time.sleep(3)
        print("Payment accepted!")
        print()
        time.sleep(1.25)
        print(f"Your change is £{change:.2f}")
        print()
        time.sleep(1.5)
        print(f"Here is your {item}, Thank you for your purchase!")
        print()
        paid = True
        time.sleep(1.25)
        break

print()