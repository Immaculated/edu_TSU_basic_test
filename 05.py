# function declaration
def print_fio(name, surname, patronymic):
    print('initials: ',
    surname[0].title(), name[0].title(), patronymic[0].title(), sep="")
# data input
    name = input('enter ur name: ')
    surname = input('enter ur surname: ')
    patronymic = input('enter ur patronymic: ')
# output check
    print('initials: ', 
    surname[0].title(), name[0].title(), patronymic[0].title(), sep="")
# function call
print_fio('juAn', 'goNzaleZ', 'AlvaRez')