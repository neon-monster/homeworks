# 4
prices = [0]
while len(prices) < 20:
    prices.append(prices[-1]+0.7)

v_odnu_stroku = ''

for i, x in enumerate(prices, start=1):
    spl_str = f'{x:.2f}'.split('.')
    if len(spl_str) != 1:
        phrase = f'{spl_str[0]} руб {int(spl_str[1]): 02d} коп'
    else:
        phrase = f'{spl_str[0]} руб 00 коп'
    if i!= len(prices):
        v_odnu_stroku = f'{v_odnu_stroku} {phrase},'
    else:
        v_odnu_stroku = f'{v_odnu_stroku} {phrase}'

print(v_odnu_stroku)
prices.sort()
print(f'сортировка по возрастанию: {prices}')
prices.sort(reverse=True)
print(f'сортировка по убыванию: {prices}')