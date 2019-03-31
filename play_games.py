import common
import hangman_game
import guessing_game

common.head("Escolha o seu jogo")

print("(1) Forca\n(2) Adivinhação")

game = int(input("Jogo: "))

if(game == 1):
    hangman_game.play()
elif(game == 2):
    guessing_game.play()
else:
    print("Opção inválida")
