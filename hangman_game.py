import common
import random


def play():
    common.head("Jogo da Forca")
    filename = get_subject_filename()
    secret_word = get_secret_word(filename)
    right_letters = initializing_correct_letters(secret_word)
    print(right_letters)

    hanged = False
    hit = False
    errors = 0

    while (not hanged and not hit):
        guess = guessing()

        if (guess in secret_word):
            correct_guess(guess, right_letters, secret_word)
        else:
            errors += 1
            show_gallows(errors)

        hanged = errors == 7
        hit = "_" not in right_letters
        print(right_letters)

    if (hit):
        show_winner_message()
    else:
        show_loser_message(secret_word)


def get_subject_filename():
    print("Qual o tema?")
    print("(1) Animais\n(2) Países\n(3) Frutas")
    subject = int(input("Tema: "))
    if (subject == 1):
        file = "animals.txt"
    elif (subject == 2):
        file = "countries.txt"
    else:
        file = "fruits.txt"

    return file


def get_secret_word(filename="fruits.txt", first_line_valid=0):
    words = []

    with open(filename) as file:
        for line in file:
            line = line.strip()
            words.append(line)

    index = random.randrange(first_line_valid, len(words))

    word = words[index].upper()

    return word


def initializing_correct_letters(word):
    return ["_" for letter in word]


def guessing():
    guess = input("Qual letra? ")
    return guess.strip().upper()


def correct_guess(guess, correct_letters, secret_word):
    index = 0
    for letter in secret_word:
        if (guess == letter):
            correct_letters[index] = letter
        index += 1


def show_gallows(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def show_winner_message():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def show_loser_message(secret_word):
    print("Você foi enforcado!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if(__name__ == "__main__"):
    play()
