#1
for x in '15 * 3 , 15 / 3 , 15 // 2 , 15 ** 2'.split(' , '):
    print(type(eval(x)))