
# import modules
from os import system
from random import choice
from english_words import get_english_words_set

# start function on my word guessing project
def start():
        words = get_english_words_set(['web2'], lower=True)
        run = True
        my_word = ''
        while run:
            rn_word = choice(list(words))
            if len(rn_word) == 6:
                my_word = rn_word
                run = False
        sec_word = []
        err_words = []
        my_rank = 0
        step = 6
        res = False
        for _ in range(len(my_word)):
            sec_word.append('_')
        while step >= 1:
            step -= 1
            system('clear')
            print('Total Score: ', my_rank)
            print(f'You have {step} attempts left!')
            print('Secret Word: ', *sec_word)
            if len(err_words):
                print('Errors: ', *err_words)
            gues_l = input('Guess the letter: ')

            for step2 in range(6):
                if gues_l in my_word:
                    if my_word[step2] == gues_l:
                        sec_word[step2] = gues_l
                        step += 1
                else:
                    err_words.append(gues_l)
                    break
            if '_' not in sec_word:
                my_rank += step
                my_rank += 1
                break

            else:
                system('clear')
                print('Game over!')
                print('The word was: ', my_word)
