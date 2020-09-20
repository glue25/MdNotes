import pydub
import os

from pydub import AudioSegment
def GetMp3(Dir) :
    '''
    Dir : param Dir: Target Dir Name
    RL : return: A List of filename (e.g. XX.mp3)
    '''
    RL = []
    # for file in os.listdir(Dir):  # 不仅仅是文件，当前目录下的文件夹也会被认为遍历到
    #     print("file", file)
    # print('\n')
    for file in os.listdir(Dir):  # 不仅仅是文件，当前目录下的文件夹也会被认为遍历到
        file_path = os.path.join(Dir, file)
        if os.path.splitext(file_path)[1]=='.mp3' :
            # list_name.append(file_path)
            print(file_path)
            RL.append(file_path)
    return RL
def MergeMp3(LMP3,OutputName = 'output_music') :
    if len(LMP3) == 0 :
        pass
    else :
        LMP3 = [''.join((word,'.mp3')) if '.mp3' not in word else word for word in LMP3]
        LInputMusic = [AudioSegment.from_mp3(x) for x in LMP3]
        output_music = LInputMusic[0]
        for i in range(1,len(LMP3)) :
            output_music = output_music + LInputMusic[i]
        if OutputName[-4:] == '.mp3' :
            pass
        else :
            OutputName = ''.join((OutputName,'.mp3'))
        output_music.export(OutputName, format="mp3")# 前面是保存路径，后面是保存格式
        print(len(output_music), output_music.channels)# 合并音频的时长，音频的声道，1单声道，2立体声
def TestMergeMp3() :
    input_music_1 = AudioSegment.from_mp3("hello.mp3")
    input_music_2 = AudioSegment.from_mp3("end.mp3")
    #获取两个音频的响度（音量）
    input_music_1_db = input_music_1.dBFS
    input_music_2_db = input_music_2.dBFS
    # 获取两个音频的时长，单位为毫秒
    input_music_1_time = len(input_music_1)
    input_music_2_time = len(input_music_2)
    # 调整两个音频的响度一致
    db = input_music_1_db- input_music_2_db
    # if db > 0:
    #     input_music_1 += abs(dbplus)
    # elif db < 0:
    #     input_music_2 += abs(dbplus)
    # 合并音频
    print(type(input_music_1))
    output_music = input_music_1 + input_music_2
    # 简单输入合并之后的音频
    output_music.export("output_music.mp3", format="mp3")# 前面是保存路径，后面是保存格式
    
    #复杂输入合并之后的音频
    # bitrate：比特率，album：专辑名称，artist：歌手，cover：封面图片
    # output_music.export("output_music.mp3", format="mp3", bitrate="192k", tags={"album": "专辑".encode('utf-8'), "artist": "歌手".encode('utf-8')}, cover="12.jpg")#.encode('gbk').decode('utf-8')
    print(len(output_music), output_music.channels)# 合并音频的时长，音频的声道，1是单声道，2是立体声
# Dir = 'E:\CatchSound'
# print(GetMp3(Dir))

# NL = ['MusicSample\\class','MusicSample\\bot','MusicSample\\star.mp3']
# MergeMp3(NL)
