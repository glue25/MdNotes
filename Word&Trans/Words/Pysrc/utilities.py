import chardet

__ElementsNums = 3
def setOutputFileName(InputFileName) : 
    '''
    Get the output file's default name referred to a certain input file.
    '''
    Suffixes = ['.txt', '.md']
    for i in Suffixes :
        if InputFileName.endwith(i) : 
            OutputFileName = ''.join((InputFileName[:-4], '-Output', i ))
    
    return OutputFileName

def __getFilelinesGenerator(FileName, encoding = 'utf8') : 
    with open(FileName, 'r', encoding=encoding) as f :
        for i in f :
            yield i

def __ProcessRawLine(line, SplitSigns) : 
    #暂时假设不处理单词与翻译中有空格的情况。
    line = line.replace('\n', '')
    SplitSigns = list(SplitSigns)
    for i in SplitSigns[1:] : 
        line = line.replace(i, SplitSigns[0])
    elements = [x for x in line.split(SplitSigns[0]) if len(x) > 0]
    if len(elements) < __ElementsNums :
        elements.append('')
    return elements

def __ProcessMDLine(line) : 
    elements = [x.replace('\t', '').strip() for x in line.split('|')]
    return elements

def RawFile2Triad(FileName, CommentSigns = None, SplitSigns = None) : 
    '''
    Transform 'Raw' file to Triad List.
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
    TriadGenerator = (__ProcessRawLine(line, SplitSigns) for line in FilelinesGenerator)

    return TriadGenerator

def MDFile2Triad(FileName, CommentSigns = None, SplitSigns = None) :
    '''
    Transform Markdown file to Triad List.
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
    TriadGenerator = (__ProcessMDLine(line, SplitSigns) for line in FilelinesGenerator)

    return TriadGenerator


