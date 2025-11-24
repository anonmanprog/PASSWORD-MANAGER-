def password_manager_cli():
    print("Welcome to the Password Manager.")
    while True:
        print("\n--- Menu ---")
        print("1. Generate Password")
        print("2. Add Password")
        print("3. Retrieve Password")
        print("4. List Applications")
        print("5. Exit")
        c = input("Enter your choice: ")
        if c == "1":
            try:
                a = int(input("How many letters?\n"))
                b = int(input("How many symbols?\n"))
                d = int(input("How many numbers?\n"))
                print("Generated Password:", generate_password(a, b, d))
            except:
                print("Invalid input.")
        elif c == "2":
            appn = input("Application name: ")
            pw = input("Password: ")
            add_password(appn, pw)
        elif c == "3":
            appn = input("App name: ")
            print(get_password(appn))
        elif c == "4":
            print(list_applications())
        elif c == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


password_manager_cli()
