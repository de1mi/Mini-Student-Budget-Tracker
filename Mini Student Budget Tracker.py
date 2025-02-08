name=input("What is your name?  " )
print(f"Welcome, to the Budget Tracker {name}! Your surest way to become prudency. \n")

user = True
while user == True:
    try:
        income= int(input("\n To begin, please, enter your income (digits only!). \n N"))
        print("\n Now, enter your expenses as mentioned below:")
        rent = int(input("\n Rent:  N"))
        food = int(input("\n Food:  N"))
        savings = int(input("\n Savings:  N"))
        transport = int(input("\n Transport:  N"))
        subs = int(input("\n Subscriptions:  N"))
        # user = False

#Totalling all of the expenses and summming up the rent and food for variable assignment.
        expenses= rent + food + savings + transport + subs
        important=rent + food

#Provide Feedback on Spending and remaining balance.
        if expenses > income:
            print(f"\n You are overspending, {name}. You have N{expenses - income} in the red. \n")
            if important > (50/100)* expenses:
                print("\n You are overspending on Rent and/ or Food.\n")
            if savings < (40/100)* expenses:
                print("\n You should save up more!\n")
            if transport > (40/100)* expenses:
                print("\n You should try walking and burn out calories!\n")
            if subs > (20/100)* expenses:
                print("\n I also think you should cut down on your subscriptions!\n ")
        else: 
            print (f"\n You can increase your savings by {round(((income - expenses) / income) * 100, 2)}%.")
            print("\n You are prudent enough, keep it up!\n ")
            print(f"\n Your remaining balance for the month is N{income-expenses}.")

        if input("\n Do you want to run the program again? (Yes or No)"  ) == "No":
            user = False
#Returns the user to input the right format in case of errors.         
    except ValueError:
        print(f"\n Invalid input! Digits only, {name}.")
        




