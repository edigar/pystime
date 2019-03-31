import common
import random


def play():
    common.head("Jogo da Adivinhação")

    secret_number = random.randrange(1, 101)
    score = 100
    level = get_level()
    attempts = get_attempts(level)

    for turn in range(1, attempts + 1):
        print("\nTentativa: {} de {}".format(turn, attempts))
        guess = guessing()

        if(guess < 1 or guess > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        print("Voce digitou ", guess)

        hit = guess == secret_number
        bigger = guess > secret_number
        smaller = guess < secret_number

        if(hit):
            print("Voce acertou e fez {} pontos!".format(score))
            break
        else:
            if(bigger):
                print("Voce errou! O seu chute foi maior do que o número secreto")
            elif(smaller):
                print("Voce errou! O seu chute foi menor do que o número secreto")
            lost_score = abs(secret_number - guess)
            score = score - lost_score

    if(not hit):
        print("\nVocê perdeu! O número correto era {}\n".format(secret_number))


def get_level():
    print("Qual nível de dificuldade?")
    print("(1) Fácil\n(2) Médio\n(3) Difícil")
    level = int(input("Nível: "))
    return level


def get_attempts(level):
    if (level == 1):
        attempts = 20
    elif (level == 2):
        attempts = 10
    else:
        attempts = 5

    return attempts


def guessing():
    guess_str = input("Digite um número entre 1 e 100: ")
    return int(guess_str)


if(__name__ == "__main__"):
    play()

