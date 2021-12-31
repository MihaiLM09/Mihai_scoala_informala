import random

def cards():
    with open('cards.txt', 'r', encoding='utf-8') as f:
       list = [line.rstrip() for line in f]
       min_nr = len(list)
       if min_nr < 10:
           raise Exception(f"Sorry, you need a minimum of 10 cards and you have just {min_nr} cards available.")
       s_list = random.sample(list, len(list))
       random_card = random.choice(s_list)
    print(list)
    print(s_list)
    print(random_card)



cards()

























