import manage_expenses as man

def main():
    menu()
    prompt = int(input("\nPlease select your option:\n"))
    
    if prompt == 1:
        man.add_expenses()
    elif prompt == 2:
        man.view_expenses()
    elif prompt == 3:
        man.category_summary()
    elif prompt == 4:
        man.get_status()
    elif prompt == 5:
        man.spending_trend()
    else:
        print("Please select one of the options listed: 1 through 5\n")


def menu():
    print("Welcome to Track Expert:\n", \
        "[1] Add an expense\n  [2] View expenses\n [3] View categories\n  [4] Get Status\n  [5] Display Trends\n [6] Other")




if __name__ == "__main__":
    main()