
from ast import While
import random

def run():
    list_characters = []
    word = random_word()
    underscore = num_underscore(word)
    list_characters = list_word(word)

    show(underscore)
    while hay_underscore(word, underscore):
        user_char = input('Ingrese una letra: ')
        coincidencia(user_char,word,underscore)
        show(underscore)
    
    print('ganaste')

def show(underscore):
    print('\n  '+' '.join(map(str, underscore)) + '\n')

        

def coincidencia(user_char,word,underscore):
    for i in range(len(word)):
        if word[i] ==user_char:
            underscore[i] = word[i]

def hay_underscore (word,underscore):
    for i in range(len(word)):
        if underscore[i] == '_':
            return True

    return False

def list_word(word):
    list_characters = []
    for i in range(len(word)):
        list_characters.append(word[i]) 
    return list_characters

def num_underscore(word):
    underscore =[]
    for x in range(len(word)):
        underscore = underscore  + ['_']
    return underscore


def random_word():
    words = []
    with open("./files/words.txt","r",encoding='utf_8') as f:
        for line in f:
            words.append(line)
    return random.choice(words).strip()


if __name__ =='__main__':
    run()