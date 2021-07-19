with open('test.txt', 'w') as nf:
    nf.write('248 256 472 456 725 2394 824 42934 234 57568 434')
nf.close()
with open('test.txt', 'r') as mf:
    print(sum(map(int, mf.readline().split())))

