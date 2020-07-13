
import argparse
import os
from itertools import tee

from Pysrc.parameters import *
from Pysrc.File_utilities import *
from Pysrc.utilities import *
from main import *
def ProcessParas2() :
    arg = process_args()
    # InputPhase = arg.inp
    OutputPhase = arg.outp

    # get Sort mod
    if 'n' in OutputPhase :
        SortMode = 'importance'
    elif 'ws' in OutputPhase :
        SortMode = 'character'
    else :
        SortMode = 'ignore'
    # print(SortMode)

    # get input/output dir

    Inputdir = arg.indir
    Outputdir = arg.outdir
    
    # check dir
    if not os.path.exists(Inputdir) :
        raise ValueError('Inputdir not exists')
    # if not os.path.exists(Outputdir) :
    #     Outputdir = DefaultOutputDir
    if (Outputdir is None) or (Outputdir=='') :
        pass
    else :
        if not os.path.exists(Outputdir) :
            os.makedirs(Outputdir)
    # if not os.path.exists(Outputdir) :
    #     if (Outputdir is None) or (Outputdir=='') : 
    #         pass
    #     else :
    #         os.makedirs(Outputdir)

    # print('------------------')
    # print(Outputdir)
    # print(os.path.exists(Outputdir))
    # print('------------------')
    InputdirIsFile = os.path.isfile(Inputdir)
    OutputdirIsFile = '.' in Outputdir#os.path.isfile(Outputdir)
    OutputdirExist = os.path.exists(Outputdir)
    # print(OutputdirIsFile)
    # assert 1== 0

    if InputdirIsFile : 
        if not OutputdirExist :
            Outputdir = setOutputFileName(Inputdir, OutputPhase)
        return SortMode, OutputPhase, Inputdir, Outputdir
    else :
        #get filename generator
        InputFileName_ = next(os.walk(Inputdir))
        InputFileNameGenerator = (os.path.join(InputFileName_[0],x) for x in InputFileName_[2])
        InputFileNameGenerator, tmpG = tee(InputFileNameGenerator)
        if not OutputdirExist :
            OutputFileNameGenerator = (setOutputFileName(x, OutputPhase) for x in tmpG)
            return SortMode, OutputPhase, InputFileNameGenerator, OutputFileNameGenerator
        else :
           if not OutputdirIsFile :
                # print('mvm-----------------')
                # print(Outputdir)
                # print('mvm-----------------')
                OutputFileNameGenerator = (setOutputFileName(x, OutputPhase,Outputdir) for x in tmpG)
                #
                # OutputFileNameGenerator,tp = tee(OutputFileNameGenerator)
                # for i in tp :
                #     print(i)
                #
                return SortMode, OutputPhase, InputFileNameGenerator, OutputFileNameGenerator
           else :
                # print('mvo-----------------')
                # print('mvo-----------------')
                # print(Outputdir)
                return SortMode, OutputPhase, InputFileNameGenerator, Outputdir
def test_main() :
    SortMode, OutputPhase, InputFileName, OutputFileName = ProcessParas2()
    
    if iter(InputFileName) is InputFileName :
        if iter(OutputFileName) is OutputFileName :
            #多对多
            for inFile, OutFile in zip(InputFileName, OutputFileName) : 
                print('***MvM***')
                print(inFile)
                print(OutFile)
                print('***MvM***')
        else :
            #多对一
            # TriadGeneratorDict = {}
            for inFile in InputFileName : 
                print(inFile)
            print(OutputFileName)

    else :
        #一对一
        assert os.path.exists(InputFileName)
        print('===OvO===')
        print(InputFileName)
        print(OutputFileName)
        print('===OvO===')
        
test_main()