with open('empl.txt', 'r') as work_file:
    salary = []
    lower = []
    my_list = work_file.read().split()
    f = 1
    for i in my_list:
        f += 2
        salary.append(my_list[f])
        if int(my_list[f]) < 20000:
            lower.append(my_list[f - 1])
        if len(my_list) == f or len(my_list) == f + 1:
            break
print(f'Оклад меньше 20000 у - {lower}, средний оклад - {sum(map(int, salary)) / len(salary)}')


