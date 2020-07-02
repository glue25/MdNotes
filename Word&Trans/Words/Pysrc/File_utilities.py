import chardet
import re
import copy
from itertools import tee

from Pysrc.parameters import * 
def setOutputFileName(InputFileName, OutputPhase) : 
    '''
    Get the output file's default name referred to a certain input file.
    '''
    Suffixes = ['.txt', '.md']
    for i in Suffixes :
        # print(InputFileName.__dir__())
        # for in InputFileName.__dir__() :
        if InputFileName.endswith(i) : 
            OutputFileName = ''.join((InputFileName[:-4], '-Output', i ))
    if Phase.IsLegalMDOutputPhase(OutputPhase) :
        OutputFileName = OutputFileName.replace('.txt','.md')
        OutputFileName = OutputFileName.replace('RawWords','MdWords')
    else : 
        OutputFileName.replace('.md','.txt')

    return OutputFileName

def __getFilelinesGenerator(FileName, encoding = 'utf8') : 
    with open(FileName, 'r', encoding=encoding) as f :
        for i in f :
            # print(len(i))
            if len(i.replace('\n',''))>0:
                yield i

def __ProcessRawLine(line, SplitSigns) : 
    #暂时假设不处理单词与翻译中有空格的情况。
    line = line.replace('\n', '')
    SplitSigns = list(SplitSigns)
    for i in SplitSigns[1:] : 
        line = line.replace(i, SplitSigns[0])
    elements = [x.strip() for x in line.split(SplitSigns[0]) if len(x) > 0]
    if len(elements) < ELEMENTS_NUM :
        elements.append('')
    return elements

def __ProcessMDLine(line) : 
    elements = [x.replace('\t', '').strip() for x in line.split('|')][1:-1]
    return elements

def RawFile2Triad(FileName, CommentSigns = None, SplitSigns = None) : 
    '''
    Transform 'Raw' file to Triad Generator.
    '''
    if CommentSigns is None :
        CommentSigns = set()
    if SplitSigns is None :
        SplitSigns = ('\t', '  ')
    with open(FileName, 'rb') as f :
        SampleData = f.read(500)
        f.seek(0)
        encoding = chardet.detect(SampleData)['encoding']
    FilelinesGenerator = __getFilelinesGenerator(FileName, encoding)
    TriadGenerator = (__ProcessRawLine(line, SplitSigns) for line in FilelinesGenerator)

    return TriadGenerator

def MDFile2Triad(FileName, CommentSigns = None, SplitSigns = None) :
    '''
    Transform Markdown file to Triad Generator.
    '''
    if CommentSigns is None :
        CommentSigns = set()
    if SplitSigns is None :
        SplitSigns = ('\t', ' ')
    with open(FileName, 'rb') as f :
        SampleData = f.read(500)
        f.seek(0)
        encoding = chardet.detect(SampleData)['encoding']
    
    FilelinesGenerator = __getFilelinesGenerator(FileName, encoding)

    # filter the header
    FilelinesGenerator = (x for x in FilelinesGenerator if len(re.sub('[ |\t\-\n]','',x))>0)
    TriadGenerator = (__ProcessMDLine(line) for line in FilelinesGenerator)

    return TriadGenerator

def Triad2MDFile(FileName, TriadGenerator) :
    '''
    Transform Generator List to Markdown file.
    '''
    with open(FileName, 'w', encoding='utf8') as f :
        f.write('| | | |')
        f.write('\n')
        f.write('|---|---|---|')
        f.write('\n')
        for i in TriadGenerator :
            f.write('|'.join(['']+i+['']))
            f.write('\n')

def Triad2RawFile(FileName, TriadGenerator) :
    '''
    Transform Generator List to Raw file.
    '''
    
    TriadGenerator, TriadGeneratorO = tee(TriadGenerator)

    Length = [0 for x in range(ELEMENTS_NUM-1)]
    for i in TriadGeneratorO :
        for j in range(ELEMENTS_NUM-1) :
            if len(i[j])>Length[j] : 
                Length[j] = len(i[j])
    # Length0 = max([len(x[0] for x in TriadGeneratorO)])
    # Length1 = max([len(x[1] for x in TriadGeneratorO)])

    Length0 = Length[0] + 2
    Length1 = int(Length[1]*9/5) + 2
    print(Length1)

    with open(FileName, 'w', encoding='utf8') as f :
        for i in TriadGenerator :
            f.write(''.join((i[0].ljust(Length0), i[1].ljust(Length1-int(len(i[1])*4/5)),i[2])))
            f.write('\n')

