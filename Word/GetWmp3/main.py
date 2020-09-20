'''
Only used to deal with D35.txt
'''
import multiprocessing
import Mp3Task
import CatchWordHTML
import multiprocessing
def GetWordMp3(L, Filename, Dir = '') :
    # for word in L :
    #     CatchWordHTML.DownloadMp3(word,'DownloadMp3\\')
    CatchWordHTML.DownloadMp3List(L,'DownloadMp3\\',NoRenewMod = True)
    # [CatchWordHTML.DownloadMp3(word,'DownloadMp3\\',NoRenewMod = True) for word in L]
    L = [''.join(('DownloadMp3\\', word)) for word in L]
    Mp3Task.MergeMp3(L, ''.join((Dir, Filename)))
def GetWordList(Filename):
    L = ''
    WordFilename = ''
    with open(Filename,'r') as f:
        for Line in f.readlines() :
            if '#' in Line :
                if WordFilename !='':
                    L = [word for word in L if word != '']
                    GetWordMp3(L, WordFilename, Dir='WordMp3\\')
                L = []
                WordFilename = Line[1:-1]
                continue
            else :
                L.append(Line[:-1]) #获取单词列表
        L = [word for word in L if word != '']
        L = [word[:-1] if word[-1]=='\n' else word for word in L]
        print(len(L),L)
        GetWordMp3(L, WordFilename, Dir='WordMp3\\')

def GetAllWordList(Filename):
    L = []
    with open(Filename,'r') as f:
        for Line in f.readlines() :
            if '#' in Line :
                pass
            else :
                L.append(Line[:-1]) #获取单词列表
    L = [word for word in L if word != '']
    CatchWordHTML.DownloadMp3List(L,'DownloadMp3\\',NoRenewMod = True)

Filename = 'C:\\Users\\admin\\Desktop\\D35.txt'
# GetAllWordList(Filename)
GetWordList(Filename)

def DownloadMp3List