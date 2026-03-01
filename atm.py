id = ""
id = int(input("Enter your account no::"))

password = "1234"
APass = input("Enter password::")
while  password != APass:
 APass=input("wrong password please re-Enter ")
 
print("Access grented !!! Account number::",id)
if password==APass:
    print("...................")
    print(" :    Menu   :")
    print("0  check balance")
    print("1  deposit")
    print("2  withdrawal")
    print("....................")
    choice=input("enter choice..")
    
    if choice==0:
       AccB=[1000]
    for i in AccB:
        print(" acc balance ", i)
     ......................................
# Transaction Counter System

def transaction_counter(transactions):
    # 1️⃣ Total Balance
    total_balance = 0

    # 2️⃣ Highest Withdrawal
    highest_withdrawal = None  # abhi tak koi withdrawal nahi

    # 3️⃣ Maximum Consecutive Deposits (Kadane variation)
    current_deposit_sum = 0
    max_deposit_sum = 0

    for amount in transactions:
        # Total balance
        total_balance += amount

        # Highest withdrawal
        if amount < 0:
            if highest_withdrawal is None or amount < highest_withdrawal:
                highest_withdrawal = amount

        # Kadane for deposits only
        if amount > 0:
            current_deposit_sum += amount
            if current_deposit_sum > max_deposit_sum:
                max_deposit_sum = current_deposit_sum
        else:
            current_deposit_sum = 0  # chain break

    if highest_withdrawal is None:
        highest_withdrawal = 0

    return total_balance, highest_withdrawal, max_deposit_sum


# 🔹 Main Program
transactions = list(map(int, input("Enter transactions separated by space: ").split()))

total, highest_wd, max_deposits = transaction_counter(transactions)

print("\n--- ATM Transaction Analysis ---")
print("Total Balance:", total)
print("Highest Withdrawal:", highest_wd)
print("Maximum Consecutive Deposits Sum:", max_deposits)
    
