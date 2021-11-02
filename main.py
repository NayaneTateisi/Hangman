# Hangman Game (Jogo da Forca)


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
        == == == ==  ''', '''
        + ------+
        |       0
        |
        |
        |
        |
        == == == ==  ''', ''''
        + ------+
        |        0
        |        |
        |
        |
        |
        == == == ==  ''', '''
        + ------+
        |        0
        |      / |
        |
        |
        |
        == == == == ''', '''
        + ------+
        |       0
        |     / | \\
        |
        |
        |
        == == == == ''', '''
        + ------+
        |       0
        |     / | \\
        |      /
        |
        |
        == == == == ''', '''
        + ------+
        |       0
        |     / | \\
        |      / \\
        |
        |
        == == == == ''']


def rand_word():
       with open("Hangman/palavras.txt", "rt") as f:
              bank = f.readlines()
       return bank[random.randint(0, len(bank))].strip()


class Hangman:

	# Select random wordl
       def __init__(self, word):
              self.word = word
              self.letters_wrong = []
              self.letters_right = []
              self.game = 0
              

       # Print the board
       def game_board(self):
	       os.system('clear')
	       print('========= Hangman Game ========= ')
	       print(board[len(self.letters_wrong)])
	       print('Letras incorretas:', self.letters_wrong)
	       print('Palavra:' + self.print_the_board() + '\n')
              

       # print the word in the board
       def print_the_board(self):
              lines = ''
                                       
              for letter in self.word:
                     if letter in self.letters_right:
                            lines += letter
                           
                     else:
                            lines += ' _' 
              
              #print('Palavra:' + lines+ '\n')
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
              if len(self.letters_wrong) == len(board):

                    print('\nFim de jogo. Você perdeu!')
                    print('''
                                  *****************
                                 * Morto     farofa *
                                 *       com        *
                            \ 0 / *****************
                            ------
                              |
                             / \                     ''')
                    print('  ')
                    print('A palavra correta era:' + self.word+ '\n')
                    return False
              elif ' _'  not in self.print_the_board():
                    print('A palavra correta é:' + self.print_the_board() + '\n')
                    print('Parabéns tu ganhasse!!')
                    print('  ')
                    print('''
                                  *********
                                 * UHULL!! *
                            \ 0 / *********
                              |
                             / \                     ''')
                    print('  ')
                    return False
       
              else:
                    return True

     


       

# create a new object
def main():
       game = Hangman(rand_word())
       while game.print_game_status():
              game.print_the_board()
              game.game_board()	
              user_input = input('Digite uma letra: ').lower()
              game.check_letter(user_input)
              
                  

main()
