my_list = ['Intel\n', 'AMD\n', 'Geforce\n', 'Mac\n']
with open("file1.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("file1.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} букв в строке")
    print(f"Кол-во строк - {lines}")