import chardet
import re
import copy
import os
from itertools import tee

from Pysrc.parameters import * 
def setOutputFileName(InputFileName, OutputPhase,*,Dir=None) : 
    '''
    Get the output file's default name referred to a certain input file.
    '''
    Suffixes = ['.txt', '.md']
    for i in Suffixes :
        if InputFileName.endswith(i) : 
            OutputFileName = ''.join((InputFileName[:-4], '-Output', i ))
    if Phase.IsLegalMDOutputPhase(OutputPhase) :
        OutputFileName = OutputFileName.replace('.txt','.md')
        OutputFileName = OutputFileName.replace('RawWords','MdWords')
    else : 
        OutputFileName.replace('.md','.txt')
        OutputFileName = OutputFileName.replace('MdWords','RawWords')

    return OutputFileName

# def getfilemod(filename) :
#     score = 0
#     if filename.endswith('.txt') :
#         score += 1
#     elif filename.endswith('.md') :
#         score -= 1
#     else : 
#         pass

#     with open

def _getFilelinesGenerator(FileName, encoding = 'utf8', CommentSigns = None) : 
    if CommentSigns is None :
        CommentSigns = set()
    with open(FileName, 'r', encoding=encoding) as f :
        for i in f :
            # print(len(i))
            #考虑删除行注释
            if i[0] not in CommentSigns :
                if len(i.replace('\n',''))>0:
                    yield i

def _ProcessRawLine(line, SplitSigns) : 
    #暂时假设不处理单词与翻译中有空格的情况。
    line = line.replace('\n', '')
    SplitSigns = list(SplitSigns)
    for i in SplitSigns[1:] : 
        line = line.replace(i, SplitSigns[0])
    elements = [x.strip() for x in line.split(SplitSigns[0]) if len(x) > 0]
    if len(elements) < ELEMENTS_NUM :
        elements.append('')
    return elements

def _ProcessMDLine(line) : 
    elements = [x.replace('\t', '').strip() for x in line.split('|')][1:-1]
    return elements

def _DetectEncodingandMode(filename) :
    #get encoding
    with open(filename, 'rb') as f :
        SampleData = f.read(500)
        f.seek(0)
        encoding = chardet.detect(SampleData)['encoding']

    score = 0
    if filename.endswith('.txt') :
        score += 1
    elif filename.endswith('.md') :
        score -= 1
    else : 
        pass
    s = SampleData.decode(encoding)
    s = re.sub('[ \n]','',s)
    if '||' in s :
        score -= 0.5
    if ('|-' in s) and ('-|' in s) : 
        score -= 0.6
    
    if s.count('|') > 6:
        score -= 0.5
    if score < 0 :
        IsMd = True
    else :
        IsMd = False
    return encoding, IsMd

def File2Triad(FileName, CommentSigns = None, SplitSigns = None) :
    encoding, IsMd = _DetectEncodingandMode(FileName)

    if CommentSigns is None :
        CommentSigns = set()
    if SplitSigns is None :
        SplitSigns = ('\t', '  ')
        
    FilelinesGenerator = _getFilelinesGenerator(FileName, encoding, CommentSigns)
    
    if IsMd : 
        FilelinesGenerator = (x for x in FilelinesGenerator if len(re.sub('[ |\t\-\n]','',x))>0)
        TriadGenerator = (_ProcessMDLine(line) for line in FilelinesGenerator)
    else :
        TriadGenerator = (_ProcessRawLine(line, SplitSigns) for line in FilelinesGenerator)

def _WriteMDFile(f, TriadGenerator) :
    '''
    Write TriadGenerator to f.
    '''
    f.write('| | | |')
    f.write('\n')
    f.write('|---|---|---|')
    f.write('\n')
    for i in TriadGenerator :
        f.write('|'.join(['']+i+['']))
        f.write('\n')


def Triad2MDFile(FileName, TriadGenerator) :
    '''
    Transform Generator List to Markdown file.
    '''
    with open(FileName, 'w', encoding='utf8') as f : 
        _WriteMDFile(f, TriadGenerator)

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
    # print(Length1)

    with open(FileName, 'w', encoding='utf8') as f :
        for i in TriadGenerator :
            f.write(''.join((i[0].ljust(Length0), i[1].ljust(Length1-int(len(i[1])*4/5)),i[2])))
            f.write('\n')

def _getMdModeName(FileName) :
    return os.path.split(FileName)[-1].split('.')[0]

def Triads2MDFile(FileName, TriadGeneratorDict) : 
    with open(FileName, 'w', encoding='utf8') as f :
        #key是文件名/路径，value是生成器
        for key, value in TriadGeneratorDict.items() :
            f.write('# %s\n'%_getMdModeName(key))
            _WriteMDFile(f, value)
            f.write('\n')

def Triads2MDFile(FileName, TriadGeneratorDict) : 
    with open(FileName, 'w', encoding='utf8') as f :
        #key是文件名/路径，value是生成器
        for key, value in TriadGeneratorDict.items() :
            f.write('# %s\n'%_getMdModeName(key))
            _WriteMDFile(f, value)
            f.write('\n')



# def RawFile2Triad(FileName, CommentSigns = None, SplitSigns = None) : 
#     '''
#     Transform 'Raw' file to Triad Generator.
#     '''
#     # if CommentSigns is None :
#     #     CommentSigns = set()
#     # if SplitSigns is None :
#     #     SplitSigns = ('\t', '  ')
#     # with open(FileName, 'rb') as f :
#     #     SampleData = f.read(500)
#     #     f.seek(0)
#     #     encoding = chardet.detect(SampleData)['encoding']
#     FilelinesGenerator = _getFilelinesGenerator(FileName, encoding, CommentSigns)
#     TriadGenerator = (_ProcessRawLine(line, SplitSigns) for line in FilelinesGenerator)

#     return TriadGenerator

# def MDFile2Triad(FileName, CommentSigns = None, SplitSigns = None) :
#     '''
#     Transform Markdown file to Triad Generator.
#     '''
#     # if CommentSigns is None :
#     #     CommentSigns = set()
#     # if SplitSigns is None :
#     #     SplitSigns = ('\t', ' ')
#     # with open(FileName, 'rb') as f :
#     #     SampleData = f.read(500)
#     #     f.seek(0)
#     #     encoding = chardet.detect(SampleData)['encoding']
    
#     FilelinesGenerator = _getFilelinesGenerator(FileName, encoding)

#     # filter the header
#     FilelinesGenerator = (x for x in FilelinesGenerator if len(re.sub('[ |\t\-\n]','',x))>0)
#     TriadGenerator = (_ProcessMDLine(line) for line in FilelinesGenerator)

#     return TriadGenerator
