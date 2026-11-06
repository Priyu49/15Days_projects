# Day 01: MindMate Interactive Menu

while True:

    print("\n========== WELCOME TO MINDMATE ==========")

    print("1. About MindMate")
    print("2. Productivity Tips")
    print("3. Check Goal Eligibility")
    print("0. Exit")

    print("========================================")

    choice = input("Enter your choice: ")

    # Option 1
    if choice == "1":

        print("\n--- ABOUT MINDMATE ---")
        print("MindMate is a personal productivity assistant.")
        print("It helps users organize tasks and achieve goals.")

    # Option 2
    elif choice == "2":

        print("\n--- PRODUCTIVITY TIPS ---")
        print("1. Create a daily task list.")
        print("2. Prioritize important tasks.")
        print("3. Avoid unnecessary distractions.")
        print("4. Take regular breaks.")
        print("5. Track your daily progress.")

    # Option 3
    elif choice == "3":

        print("\n--- GOAL ELIGIBILITY CHECK ---")
        tasks = int(input("How many tasks do you plan to complete today? "))
        if tasks >= 5:
            print("Great! You have an ambitious daily goal.")

        elif tasks >= 1:

            print("Good! Your daily goal is achievable.")

        elif tasks == 0:

            print("You haven't planned any tasks yet.")

        else:

            print("Please enter a valid number.")

    # Exit
    elif choice == "0":

        print("\nThank you for using MindMate!")
        print("Have a productive day!")
        break

    else:

        print("\nInvalid choice! Please try again.")