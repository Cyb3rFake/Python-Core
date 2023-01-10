"""Угадайка слов(Hangman)"""
import random
word_list = ['год',
       'человек',
       'время',
       'дело',
       'жизнь',
       'день',
       'рука',
       'раз',
       'работа',
       'слово',
       'место',
       'лицо',
       'друг',
       'глаз',
       'вопрос',
       'дом',
       'сторона',
       'страна',
       'мир',
       'случай',
       'голова',
       'ребенок',
       'сила'
       ]

def get_word():
       word = random.choice(word_list)
       return word.upper()

def check_input(inp='asdf'):
       if inp.isalpha() == False:
              print('Введите корректное значение')
       else:
              pass


def display_hangman(tries = 6):
       stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
              '''
                 --------
                 |      |
                 |      O
                 |     \\|/
                 |      |
                 |     / \\
                 -
              ''',
              # голова, торс, обе руки, одна нога
              '''
                 --------
                 |      |
                 |      O
                 |     \\|/
                 |      |
                 |     / 
                 -
              ''',
              # голова, торс, обе руки
              '''
                 --------
                 |      |
                 |      O
                 |     \\|/
                 |      |
                 |      
                 -
              ''',
              # голова, торс и одна рука
              '''
                 --------
                 |      |
                 |      O
                 |     \\|
                 |      |
                 |     
                 -
              ''',
              # голова и торс
              '''
                 --------
                 |      |
                 |      O
                 |      |
                 |      |
                 |     
                 -
              ''',
              # голова
              '''
                 --------
                 |      |
                 |      O
                 |    
                 |      
                 |     
                 -
              ''',
              # начальное состояние
              '''
                 --------
                 |      |
                 |      
                 |    
                 |      
                 |     
                 -
              '''
       ]
       return stages[tries]

def play(word = 'тест'):
       word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
       guessed = False                    # сигнальная метка
       guessed_letters = []               # список уже названных букв
       guessed_words = []                 # список уже названных слов
       tries = 6                          # количество попыток
       print('Начнем игру')
       # print(word)
       print(f'Загаданно слово {word_completion} ({len(word)})букв')
       print(f'У Вас {tries} попыток')
       while not guessed and tries > 0:
              guess = input('Введите букву или слово целиком: ').upper()
              if len(guess) == 1 and guess.isalpha():
                     if guess in guessed_letters:
                            print('Вы уже называли букву', guess)
                     elif guess not in word:
                            print('Буквы', guess, 'нет в слове.')
                            tries -= 1
                            guessed_letters.append(guess)
                     else:
                            print('Отличная работа, буква', guess, 'присутствует в слове!')
                            guessed_letters.append(guess)
                            word_as_list = list(word_completion)
                            indices = [i for i in range(len(word)) if word[i] == guess]
                            for index in indices:
                                   word_as_list[index] = guess
                            word_completion = ''.join(word_as_list)
                            if '_' not in word_completion:
                                   guessed = True
              elif len(guess) == len(word) and guess.isalpha():
                     if guess in guessed_words:
                            print('Вы уже называли слово', guess)
                     elif guess != word:
                            print('Слово', guess, 'не является верным.')
                            tries -= 1
                            guessed_words.append(guess)
                     else:
                            guessed = True
                            word_completion = word
              else:
                     print('Введите букву или слово.')
              print(display_hangman(tries))
              print(word_completion)
              print()
       if guessed:
              print('Поздравляем, вы угадали слово! Вы победили!')
       else:
              print('Вы не угадали слово. Загаданным словом было ' + word + '. Может быть в следующий раз!')


if __name__ == '__main__':
       play(get_word())

