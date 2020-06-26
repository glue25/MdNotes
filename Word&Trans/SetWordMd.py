def SortMd(filename, c1 = '*', c2 = '=') :
    filename2 = filename[:-3]+'Pri.md'
    with open(filename, 'r', encoding = 'utf8') as f:
        L = f.readlines()
        LHead = L[:2]
        L = L[2:]
        L1 = sorted([x for x in L if c1 in x])
        L2 = sorted([x for x in L if (c1 not in x) and (c2 not in x)])
        L3 = sorted([x for x in L if c2 in x])
        L = LHead + L1 + L2 + L3
    with open(filename2, 'w', encoding = 'utf8') as f:
        f.writelines(L)
SortMd('论文单词积累-Sorted0316Pri.md')