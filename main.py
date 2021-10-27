# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
import os

# Board (tabuleiro)
board = ['''
         + ------+
         |       |
         |
         |
         |
         |
         == == == == = ''', '''
        + ------+
        |       0
        |
        |
        |
        |
        == == == == = ''', ''''
        + ------+
        |        0
        |        |
        |
        |
        |
        == == == == = ''', '''
        + ------+
       |        0
       |      / |
       |
       |
       |
       == == == == =''', '''
       + ------+
       |       0
       |     / | \\
       |
       |
       |
       == == == == =''', '''
       + ------+
       |       0
       |     / | \\
       |      /
       |
       |
       == == == == =''', '''
       + ------+
       |       0
       |     / | \\
       |      / \\
       |
       |
       == == == == =''']


def rand_word():
       with open("palavras.txt", "rt") as f:
              bank = f.readlines()
       return bank[random.randint(0, len(bank))].strip()


class Hangman:

	# Select random wordl
       def __init__(self, word):
              self.word = word
              self.letters_wrong = []
              self.letters_right = []
              self.game = 0
              print(word)

       # Print the board
       def game_board(self):
	       print(board[len(self.letters_wrong)])
              
            
       # print the word in the board
       def print_the_board(self):
              lines = ''
              checkStatus = len(self.word)
                         
              for letter in self.word:
                     if letter in self.letters_right:
                            lines += letter
                           
                     else:
                            lines += ' _' 
              print('Palavra:' + lines+ '\n')
              return lines
              # return print('Palavra:' + lines+ '\n') 

       #check the letter

       def check_letter(self,input):
              if input in self.word:
                     self.letters_right.append(input)


              else:
                     self.letters_wrong.append(input)
                     print(len(self.letters_wrong))
                            
              



       # Check the game status
       def print_game_status(self):
              # os.system('clear')
              if len(self.letters_wrong) == 7:
                    print('\n Fim de jogo. Você perdeu!')
                    return False
              elif ' _'  not in self.print_the_board():
                    print('ganhasse')
       
              else:
                    return True

     


       

# create a new object
def main():
       game = Hangman(rand_word())
       while game.print_game_status():
              game.game_board()	
              print(' ')
              game.print_the_board()
              

              user_input = input('Digite uma letra: ').lower()
              game.check_letter(user_input)
              
                  

main()



