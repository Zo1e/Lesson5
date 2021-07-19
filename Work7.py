import json
profit = {}
pr = {}
prof = 0
average_profit = 0
i = 0
with open('for7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        average_profit = prof / i
        print(f'Средняя прибыль - {average_profit:.2f}')
    else:
        print(f'Средняя прибыль отсутствует, компании работают в убыток.')
    pr = {'Средняя прибыль': round(average_profit)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json содержащий следующее: \n '
          f' {js_str}')
