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
    