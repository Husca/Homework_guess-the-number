import functions_game

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

    select = selection.capitalize()

    if select == "A":
        functions_game.play_game()
    elif select == "B":
        print("Game level: (A) Easy level | (B) Medium level | (C) Hard level")
        functions_game.top_score()
    else:
        break

