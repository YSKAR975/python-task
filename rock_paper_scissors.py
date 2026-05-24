name1 = input("Enter your name: ")

name2 = input("Enter your name: ")

player1_score = 0

player2_score = 0
while True:
    player1_option = input(f"{name1} chosse one of rock, paper, scissor: ")

    while player1_option not in ("rock, paper, scissor"):
        print("warning, incorrect answer write again ")
        player1_option = input("chosse one of rock, paper, scissor:")
    print("correct answer")

    for i in range(1, 20, 1):
        print()

    player2_option = input(f"{name2}chosse one of rock, paper,scissor: ")
    while player2_option not in ("rock, paper, scissor"):
        print("warning, incorrect answer write again ")
        player2_option = input("chosse one of rock, paper, scissor:")
    print("correct answer")

    if player1_option == "rock" and player2_option == "scissor" or player1_option == "paper" and player2_option == "rock" or player1_option == "scissor" and player2_option == "paper":
        print(f"{name1} has won")
        player1_score += 1

    elif player2_option == "rock" and player1_option == "scissor" or player2_option == "scissor" and player1_option == "paper" or player2_option == "scissor" and player1_option == "paper":
        print(f"{name2} has won")
        player2_score += 1

    else:
        print("equal")
