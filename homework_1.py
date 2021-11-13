# 1
def a():
    try:
        duration = int(input('введите числовое значение \n'))
        one_day = 60 * 60 * 24
        one_hour = 60 * 60
        one_min = 60
        days = duration // one_day
        hours = (duration % one_day) // one_hour
        minutes = (duration % one_hour) // one_min
        sec = duration % one_min
        out_str = ''

        if days:
            out_str = out_str + str(days) + ' дней '

        if hours:
            out_str = out_str + str(hours) + ' часов '

        if minutes:
            out_str = out_str + str(minutes) + ' минут '

        if sec:
            out_str = out_str + str(sec) + ' секунд '

        print(out_str)
    except ValueError:
        print('ошибка в введенном значении')
        a()
a()

# 2
my_cute_list = [x**3 for x in range(1, 1000, 2)]
my_cute_value = 0
my_cute_value_17 = 0
for x in my_cute_list:
    new_value = 0
    new_value_17 = 0

    for y in str(x):
        new_value += int(y)

    for y in str(x + 17):
        new_value_17 += int(y)

    if not new_value % 7:
        my_cute_value += x

    if not new_value % 7:
        my_cute_value_17 += x+17

print(my_cute_list)
print(my_cute_value)
print(my_cute_value_17)

# 3
percents = range(101)

for x in percents:

    if len(str(x)) > 1 and str(x)[0] == '1':
        print(str(x) + ' процентов')

    elif int(str(x)[-1]) == 1:
        print(str(x) + ' процент')

    elif int(str(x)[-1]) > 1 and int(str(x)[-1]) < 5:
        print(str(x) + ' процента')
    else:
        print(str(x) + ' процентов')
