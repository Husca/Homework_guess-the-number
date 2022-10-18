import datetime
import json
import random

def top_score():
    # Esta função abre ficheiro de registo de jogadas e mostra as melhores 3 classificações

    with open("score_logger.json", "r") as score_file:  # Ler ficheiro json
        best_score_list = json.load(score_file)

    sort_score = sorted(best_score_list, key=lambda k: k["Attempts"])[:3]

    for sort_dict in sort_score:
        print(f"{sort_dict}")

def play_game():
    # Esta função abre o modo jogo

    with open("score_logger.json", "r") as score_file:  # Ler ficheiro json
        best_score_list = json.load(score_file)

    current_time = datetime.datetime.now()
    attempts = 0

    Player = input("What's your name? ") # Identifica o jogador

    print("Game level: (A) Easy level | (B) Medium level | (C) Hard level")
    game_level = input("Please select your level: ") # Permite escolher o nível de jogo
    g_l = game_level.capitalize()

    if g_l == "A": # Nível de jogo fácil

        computer_guess = random.randint(1, 10)
        while True:
            guess = int(input("Guess the secret number 1 to 10: "))
            attempts += 1

            if guess == computer_guess:

                best_score_list.append({"Player": Player, "Attempts": attempts, "Game level": g_l,
                                        "Date": str(current_time)})
                with open("score_logger.json", "w") as score_file:
                    score_file.write(json.dumps(best_score_list))  # Dumps para escrever no ficheiro
                print(f"You've guessed it - congratulations! It's number {guess}")
                print(f"You got it in {attempts} attempts.")

                break

            elif guess > computer_guess:
                print("Your guess is not correct... try something smaller")

            elif guess < computer_guess:
                print("Your guess is not correct... try something bigger")

    elif g_l == "B": # Nível de jogo médio

        computer_guess = random.randint(1, 30)
        while True:
            guess = int(input("Guess the secret number 1 to 30: "))
            attempts += 1

            if guess == computer_guess:

                best_score_list.append({"Player": Player, "Attempts": attempts, "Game level": g_l,
                                        "Date": str(current_time)})
                with open("score_logger.json", "w") as score_file:
                    score_file.write(json.dumps(best_score_list))  # Dumps para escrever no ficheiro
                print(f"You've guessed it - congratulations! It's number {guess}")
                print(f"You got it in {attempts} attempts.")

                break

            elif guess > computer_guess:
                print("Your guess is not correct... try something smaller")

            elif guess < computer_guess:
                print("Your guess is not correct... try something bigger")

    elif g_l == "C": # Nível de jogo dificil

        computer_guess = random.randint(1, 50)
        while True:
            guess = int(input("Guess the secret number 1 to 50: "))
            attempts += 1

            if guess == computer_guess:

                best_score_list.append({"Player": Player, "Attempts": attempts, "Game level": g_l,
                                        "Date": str(current_time)})
                with open("score_logger.json", "w") as score_file:
                    score_file.write(json.dumps(best_score_list))  # Dumps para escrever no ficheiro
                print(f"You've guessed it - congratulations! It's number {guess}")
                print(f"You got it in {attempts} attempts.")

                break

            elif guess > computer_guess:
                print("Your guess is not correct... try something smaller")

            elif guess < computer_guess:
                print("Your guess is not correct... try something bigger")





