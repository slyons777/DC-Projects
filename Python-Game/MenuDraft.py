while True:

    print("WELCOME TO THE BLACKJACK GAME!")
    choice = int(input("""
        1. Start Game
        2. View Instructions
        3. Exit
        """))
    if choice == 1:
        play_blackjack(deck)
    elif choice == 2:
        view_instructions()
    else:
        pass

  