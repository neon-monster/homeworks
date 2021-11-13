#2
dan_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_weather = ''
len_list = len(dan_list)
for i, x in enumerate(dan_list, start=1):

    if x.isnumeric():
        new_x = int(x)
        x = f'"{new_x:02d}"'
    elif x[0] == '+' or x[0] == '-':
        new_x = int(x[1:])
        x = f'"{new_x:02d}"'

    if i != len_list:
        new_weather = new_weather + x + ' '
    else:
        new_weather = new_weather + x

print(new_weather)