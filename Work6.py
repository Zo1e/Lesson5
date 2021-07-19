subj = {}
with open('for6.txt', 'r') as nf:
    for line in nf:
        subject, lec, prac, lab = line.split()
        subj[subject] = int(lec) + int(prac) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')












