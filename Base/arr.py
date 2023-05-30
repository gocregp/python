num = 32
run = True
zagad = '?'
while run:
    guess = int(input('Введите число: - '))
    if guess == num:
        print(f'Вы угадали это число {num}!')
        run = False
    elif guess < num:
        print(f'Ваше число {guess} меньше загаданного {zagad}')
    else:
        print(f'Ваше число {guess} болньше загаданного {zagad}')