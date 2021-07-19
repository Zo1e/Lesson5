file = open('file.txt', 'w')
line = input('Введите текст - \n')
while line != '':
    file.writelines(line)
    line = input('Введите текст - \n')

file.close()

