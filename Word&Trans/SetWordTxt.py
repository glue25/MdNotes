def ResetWordTxt(Filename, SortedFilename = None) : 
    '''
    将每行按单词部分进行升序排序
    '''
    if SortedFilename is None :
        SortedFilename = ''.join((Filename[:-4], '-Sorted.txt'))
    with open(Filename, 'r', encoding = 'utf8') as OriFile :
        OLines = OriFile.readlines()
        OLines = sorted(OLines)
    with open(SortedFilename, 'w', encoding = 'utf8') as WriteFile :
        WriteFile.writelines(OLines)
def Txt2Md(filename) : 
    filename2 = filename[:-3] + 'md'
    with open(filename, 'r', encoding = 'utf8') as f :
        String = f.readlines()
        String = [''.join(('|',x[:-1],'|\n')) for x in String if x != '\n']
        for i in list(range(1,10))[::-1]:
            String = [x.replace('\t'*i,'|') for x in String] 
    with open(filename2, 'w', encoding='utf8') as f :
        f.write('| | |\n')
        f.write('| ------- | ------- |\n')
        f.writelines(String)
Txt2Md('论文单词积累-Sorted.txt')

