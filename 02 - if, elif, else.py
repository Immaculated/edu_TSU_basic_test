ages = int(input('enter completed years:\t'))
if ages >= 18:
    print('access allowed')
elif 14 <= ages <= 17:
    print('limited access')
else:
    print('access denied')
