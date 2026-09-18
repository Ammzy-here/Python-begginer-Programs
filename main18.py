Account = {"username": "Ammzy",
           "password": "123456",
           "balance" : "200000"}
 
ask=input("Enter your username: ")
pin=input("Enter your password: ")
if ask == Account["username"] and pin == Account["password"]:
    print("""Welcome To Your Account
          What You Wanna Check
          1)Username
          2)password
          3)Balance
          4)Widrawal
          5)Deposite""")
    check=input().capitalize().strip()
    if check == "Username":
        print(Account["username"])
    elif check == "Password":
        print(Account["password"])
    elif check == "Balance":
        print(Account["balance"])
    elif check == "Widrawal":
        widrawal=int(input("Enter the amount you want to widraw: "))
        if widrawal >=int(Account["balance"]):
            print("insufficient balance")
        else:
            Account["balance"] = str(int(Account["balance"]) - widrawal)
            print("Widrawal successful")
            print("Your new balance is: ", Account["balance"])
