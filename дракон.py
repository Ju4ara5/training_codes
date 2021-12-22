import random
import time


def displayIntro():
    print('''Вы находитесь в землях драконов.
Перед вами две пещеры.
В одной дружелюбный дракон, в другой - голодный.
Выбери одну.''')
    print()


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('В какую пещеру вы войдете? (нажмите 1 или 2)')
        cave = input()

    return cave


def checkCave(chosenCave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Темнота вас пугает...')
    time.sleep(2)
    print('Дракон выпрыгивает! Открывает пасть... и...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('... делится сокровищами!')
        print()
    else:
        print('... откусывает вам башку!')
        print()


playAgain = 'да'
while playAgain == 'да' or playAgain == 'д':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Пробуем ище раз? (да или нет)')
    playAgain = input()
