registers = []

while True:

    options = input("login or register: ")

    if options == "register":
        while True:
            username_register1 = input("Enter your username: ")

            if len(username_register1) < 3:
                print("incorret, write agian")
            else:
                break

        while True:
            password_register1 = input("Enter your password: ")

            if len(password_register1) < 5:
                print("incorret, write agian")
            else:
                break
        registers.append([username_register1, password_register1, 0])
        print(registers)

    if options == "login":
        username_login1 = input("Enter your username: ")
        password_login1 = input("Enter your password: ")

        while True:
            if registers[0][0] == username_login1 and registers[0][1] == password_login1:
                print("Access granted, Hello Yavzka5")
                break

        while True:
            options = input("chosse one of them (deposit, withdraw, exit, check balance) :")

            if options == "deposit":
                deposit = int(input("How much do you want to deposite: "))
                if deposit < 0:
                    print("EROR")
                    continue
                registers[0][2] = registers[0][2] + deposit

            elif options == "check balance":
                print(f"you have {registers[0][2]} money in your balance")

            elif options == "withdraw":
                print(f"you have {registers[0][2]} money in your balance")
                withdraw = int(input("How much do you want to withdraw: "))
                if withdraw > registers[0][2]:
                    print("EROR, not enough money")
                    continue
                registers[0][2] = registers[0][2] - withdraw

            elif options == "exit":
                print("See you")
                break
