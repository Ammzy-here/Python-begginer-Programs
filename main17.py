def pizza():
    print("""Flavours: Pepperoni, Mushroom, Extra Cheese """)
    print("Available Sizes: Small, Medium, Large")
    print("Would you like to order a pizza? (yes/no)")
    request=input().capitalize().strip()
    if request == "Yes":
        print("What flavour would you like?")
        flavour=input().capitalize().strip()
        match flavour:
            case "Pepperoni":
                print(f"you ordered a {flavour}")
            case "Mushroom":
                print(f"you ordered a {flavour}")
            case "Extra cheese":
                print(f"you ordered a {flavour}")
            case _:
                print("Invalid flavour")
        print("What size would you like?")
        size=input().capitalize().strip()
        match size:
            case "Small":
                print(f"You ordered a {size} {flavour} pizza.")
            case "Medium":
                print(f"You ordered a {size} {flavour} pizza.")
            case "Large":
                print(f"You ordered a {size} {flavour} pizza.")
            case _:
                print("Invalid size")
        print(f"You have ordered a {size} {flavour} pizza.")
    elif request == "No":
        print("Thank you for visiting us. Have a great day!")
   
   
     
def burger():
    print("""Flavours: Cheese, Chicken, Veggie """)
    print("Available Sizes: Small, Medium, Large")
    print("Would you like to order a burger? (yes/no)")
    request=input().capitalize().strip()
    if request == "Yes":
        print("What flavour would you like?")
        flavour=input().capitalize().strip()
        match flavour:
            case "Cheese":
                print(f"you ordered a {flavour}")
            case "Chicken":
                print(f"you ordered a {flavour}")
            case "Veggie":
                print(f"you ordered a {flavour}")
            case _:
                print("Invalid flavour")
        print("What size would you like?")
        size=input().capitalize().strip()
        match size:
            case "Small":
                print(f"You ordered a {size} {flavour} burger.")
            case "Medium":
                print(f"You ordered a {size} {flavour} burger.")
            case "Large":
                print(f"You ordered a {size} {flavour} burger.")
            case _:
                print("Invalid size")
        print(f"You have ordered a {size} {flavour} burger.")
    elif request == "No":
        print("THANKS FOR COMING HAVE A GOOD DAY")
    

def sandwich():
    print("""Options ,Chicken  , Beef ,Salad """)
    print("Avaliable Sizes Small, Medium, Large")
    print("Would you like too order Sandwich Yes/NO")
    request=input().capitalize().strip()
    if request == "Yes":
        print("what flavour do you want too order")
        flavour=input().capitalize().strip()
        match flavour:
            case "Chicken":
                print(f"You selected {flavour} Sandwich")
            case "Beef":
                print(f"You selected {flavour} Sandwich")
            case "Salad":
                print(f"You selected {flavour} Sandwich")
            case _:
                print("Invalid Entry or Flavour")
        print("What Size You like too order")
        size=input().capitalize().strip()
        match size:
            case "Small":
                print(f"You Selected {flavour} {size}Sandwich")
            case "Medium":
                print(f"You Selected {flavour} {size} Sandwich" )
            case "Large":
                print(f"you Selected {flavour} {size} Sandwich")
            case _:
                print("invalid Entry or flavour")
    elif request == "No":
        print("Thanks For Coming Have a Good Day")

def icecream():
    print("""Flavours: Vanilla, Choclate, Strawberry, Kulfa""")
    print("Cup, Cone, Family pack")
    print("Would you like to order ice cream? (yes/no)")
    request=input().strip().capitalize()
    if request == "Yes":
        print("What flavour would you like?")
        flavour=input().strip().capitalize()
        match flavour:
            case "Vanilla":
                print(f"You ordered a {flavour} ice cream.")
            case "Choclate":
                print(f"You ordered a {flavour} ice cream.")
            case "Strawberry":
                print(f"You ordered a {flavour} ice cream.")
            case "Kulfa":
                print(f"You ordered a {flavour} ice cream")
            case _:
                print("Invalid flavour")
        print("What size would you like?")
        size=input().strip().capitalize()
        match size:
            case "Cup":
                print(f"You ordered a {size} {flavour} ice cream.")
            case "Cone":
                print(f"You ordered a {size} {flavour} ice cream.")
            case "Family pack":
                print(f"You ordered a {size} {flavour} ice cream.")
            case _:
                print("Invalid size")
    
def pasta():
    Print("""Flavours: Chicken, Cheese, Peeri Peeri""")
    print("Small ,Medium, Large")
    print("Would you Like to order Yes/No")
    request=input().strip().capitalize()
    if request == "Yes":
        print("What Flavour Would you like too order")
        flavour=input().strip().capitalize().title()
        match flavour:
            case "Chicken":
                print(f"You ordered a {flavour}pasta")
            case "Cheese":
                print(f"You ordered{flavour}pasta")
            case "Peeri Peeri":
                print(f"you ordered {flavour}pasta")
            case _:
                print("Invalid Entrty")
        print("What Size do you Want")
        size=input().strip().capitalize()
        match size:
            case "Small":
                print(f"You ordered {flavour} {size} Pasta")
            case "Medium":
                print(f"You ordered {flavour} {size} Pasta")
            case "Large":
                print(f"You ordered {flavour} {size} Pasta")
            case _:
                print("Invalid Size")



a=input("What would you like too order today? (pizza, burger, sandwich, icecream,Pasta): ").capitalize()
if a == "Pizza":
    pizza()
elif a == "Burger":
    burger()
elif a == "Sandwich":
    sandwich()
elif a == "Icecream":
    icecream()
elif a == "Pasta":
    pasta()
