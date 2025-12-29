# EXPENSE TRACKER PROJECT

expense = []        #list of expenses in form of dictionaries
print("WELCOME TO EXPENSE TRACKER")
while True:
    print("==== SELECT AN OPTION ====")
    print(''' 
          1. Add Expense
          2. View expenses
          3. Total spent
          4. Delete expense
          5. exit
          ''')
    choice = int(input("enter you choice(1-5): "))

    if choice == 1:
        date = input("Enter the date (DD-MM-YYYY): ")
        title = input("enter the title of your expense: ")
        description = input("Enter the description of your expense: ")
        amount = int(input("Enter the amount spent: "))
        
        expense.append({'Date' : date,
        "Title" : title,
        "Description" : description,
        "Amount" : amount})

        print("------Expense added successfully!------")

    elif choice == 2:
        if not expense:
            print("------No expenses to show.------")
        else:
            print("------Here is your expense list: ------")
            for i,exp in enumerate(expense, start=1):
                print(f"\n{i}. Date: {exp['Date']}, Title: {exp['Title']}, Description: {exp['Description']}, Amount: {exp['Amount']}\n")
    
    elif choice == 3:
        total_spent = 0
        for exp in expense:
            total_spent += exp['Amount']
        print(f"\n------Total amount spent: {total_spent}------\n")


    elif choice == 4:
        if not expense:
            print("------No expenses to delete.------")
        else:
            print("------Here is your expense list: ------")
            for i,exp in enumerate(expense, start=1):
                print(f"\n{i}. Date: {exp['Date']}, Title: {exp['Title']}, Description: {exp['Description']}, Amount: {exp['Amount']}")
            del_index = int(input("Enter the expense number to delete: "))
            if 1 <= del_index <= len(expense):
                del expense[del_index -1]
                print("------Expense deleted successfully!------")
            else:
                print("------Invalid expense number. Enter a existing expense number.------")

    elif choice == 5:
        print("===Exiting Expense Tracker. Goodbye!===")
        print("===THANK YOU FOR USING EXPENSE TRACKER===")
        break

    else:
        print("Invalid choice. Please select a valid option(1-4)>")
        