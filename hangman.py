
import random

def run():
    random_word()


def random_word():
    words = []
    with open("./files/words.txt","r",encoding='utf_8') as f:
        for line in f:
            words.append(line)
    
    print(random.choice(words))
    

if __name__ =='__main__':
    run()