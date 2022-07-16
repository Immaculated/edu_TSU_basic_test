letters = input('enter some letters: ')
numbas = int(input('enter quantity of repetitions: '))
print(*[f'\n{letters}' for x in range(numbas)])
