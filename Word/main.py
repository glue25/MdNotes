import argparse
import os
from itertools import tee

from Pysrc.parameters import *
from Pysrc.File_utilities import *
from Pysrc.utilities import *

def process_args() :
    parser = argparse.ArgumentParser(description='Transform words.')
    parser.add_argument('-indir',help='input file dir')#, default='')
    # parser.add_argument('-inf', help='input file', default='')
    parser.add_argument('-outdir', help='output file dir')#, default='')
    # parser.add_argument('-outf', help='output file', default='')

    # parser.add_argument('-inp', help='input phase', choices=Phase.LegalInputPhase)
    parser.add_argument('-outp', help='output phase', choices=Phase.LegalOutputPhase)
    
    # parser.add_argument('-mod', help='output mod', choices=Phase.LegalSortMod, default='character')
    
    args = parser.parse_args()
    return args

def ProcessParas() :
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
    print(SortMode)

    # get input/output dir

    Inputdir = arg.indir
    Outputdir = arg.outdir
    
    # check dir
    if not os.path.exists(Inputdir) :
        raise ValueError('Inputdir not exists')
    # if not os.path.exists(Outputdir) :
    #     Outputdir = DefaultOutputDir
    if not os.path.exists(Outputdir) :
        if (Outputdir is None) or (Outputdir=='') : 
            pass
        else :
            os.makedirs(Outputdir)

    InputdirIsFile = os.path.isfile(Inputdir)
    OutputdirIsFile = os.path.isfile(Outputdir)
    OutputdirExist = os.path.exists(Outputdir)

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
                OutputFileNameGenerator = (setOutputFileName(x, OutputPhase,Outputdir) for x in tmpG)
                return SortMode, OutputPhase, InputFileNameGenerator, OutputFileNameGenerator
           else :
               return SortMode, OutputPhase, InputFileNameGenerator, Outputdir


    # if not(arg.indir or arg.inf) :
    #     raise ValueError("No useable input file address")
    # if (arg.indir == '') and (not(os.path.exists(arg.inf))) :
    #     arg.indir = 'E:\MDNotes\Word\RawWords' 
    # if arg.indir == '' and os.path.exists(arg.inf): 
    #     InputFileName = arg.inf
    # elif os.path.exists(arg.inf):
    #     InputFileName = '\\'.join((arg.indir, arg.inf))
    # else :
    #     raise ValueError('InputFile does not exist')
    
    # if not(arg.outdir or arg.outf) :
    #     OutputFileName = setOutputFileName(InputFileName,arg.outp)
    # else :
    #     OutputFileName = '\\'.join((arg.outdir, arg.outf))
    # OutputFileName = OutputFileName.lstrip('\\')
    # print(OutputFileName)

    # return SortMode, OutputPhase, InputFileName, OutputFileName

def ProcessOvO(SortMode, OutputPhase, InputFileName, OutputFileName) :
    FileTriad = File2Triad(InputFileName)
    FileTriad = SortFuncs[SortMode](FileTriad)

    if Phase.IsLegalMDOutputPhase(OutputPhase) : 
        Triad2MDFile(OutputFileName, FileTriad)
    else : 
        Triad2RawFile(OutputFileName, FileTriad)

def main() : 
    SortMode, OutputPhase, InputFileName, OutputFileName = ProcessParas()

    print('SortMode', SortMode)
    print('OutputPhase', OutputPhase)
    print('InputFileName',OutputFileName)
    print('OutputFileName',OutputFileName)
    if 
    assert 1==0
    if iter(InputFileName) is InputFileName :
        if iter(OutputFileName) is OutputFileName :
            #多对多
            for inFile, OutFile in zip(InputFileName, OutputFileName) : 
                ProcessOvO(SortMode, OutputPhase, inFile, OutFile)
        else :
            #多对一
            TriadGeneratorDict = {}
            for inFile in InputFileName : 
                TriadGeneratorDict[inFile] = File2Triad(inFile)
            if Phase.IsLegalMDOutputPhase(OutputPhase) : 
                Triads2MDFile(OutputFileName, TriadGeneratorDict)
            else :
                Triads2RawFile(OutputFileName, TriadGeneratorDict)

    else :
        #一对一
        assert os.path.exists(InputFileName)
        ProcessOvO(SortMode, OutputPhase, InputFileName, OutputFileName)


if __name__ == '__main__' : 
    main()
