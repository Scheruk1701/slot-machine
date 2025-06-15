MAX_LINES=3 #global constant

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater then 0.")
        else:
            print("Please enter a number.")
    
    return amount

def get_no_of_lines():
    while True:
        lines = input("Enter the num")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater then 0.")
        else:
            print("Please enter a number.")
    
    return amount
def main():
    balance = deposit()

main()
    