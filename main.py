
def lotto():
    import random
    number_pool = list(range(1, 90))
    computer_card = random.sample(number_pool, 15)
    computer_card_sorted = sorted(computer_card)
    player_card = random.sample(number_pool, 15)
    player_card_sorted = sorted(player_card)

import random
def card():
 def string():
  steps  = list(' ' *15)
  numbers = [' '+str(random.randint(1, 90))+' ' for x in range(5)]
  random.shuffle(string)
  print(''.join(string))
 for x in range(3):
  string()


print('Добро пожаловать в игру Лото')
name = input('Как тебя зовут?')

print('Отлично!', name)
answer = input('И так ты готов?:')

if answer == 'Да':
    lotto()
elif answer == 'Нет':
    print(('Готовься тогда)'))



