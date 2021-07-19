rus = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
with open('words.txt', 'r') as new_file:
    result = []
    for line in new_file:
        r = line.split()
        m = rus.get(r[0])
        r.pop(0)
        r.insert(0, m)
        new_r = ' '.join(r)
        result.append(new_r)

    with open('wordss.txt', 'w') as mf:
        mf.write('\n'.join(result))









