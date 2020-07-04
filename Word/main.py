import argparse
import os

from Pysrc.parameters import Phase
from Pysrc.File_utilities import *
from Pysrc.utilities import *

def process_args() :
    parser = argparse.ArgumentParser(description='Transform words.')
    parser.add_argument('-indir',help='input file dir', default='')
    parser.add_argument('-inf', help='input file', default='')
    parser.add_argument('-outdir', help='output file dir', default='')
    parser.add_argument('-outf', help='output file', default='')

    parser.add_argument('-inp', help='input phase', choices=Phase.LegalInputPhase)
    parser.add_argument('-outp', help='output phase', choices=Phase.LegalOutputPhase)
    
    # parser.add_argument('-mod', help='output mod', choices=Phase.LegalSortMod, default='character')
    
    args = parser.parse_args()
    return args

def ProcessParas() :
    arg = process_args()
    # print('arg.inf',arg.inf)
    # print('arg.outf',arg.outf)
    # get input/output phase
    InputPhase = arg.inp
    OutputPhase = arg.outp

    # get Sort mod
    if 'n' in OutputPhase :
        SortMode = 'importance'
    elif 'ws' in OutputPhase :
        SortMode = 'character'
    else :
        SortMode = 'ignore'
    print(SortMode)

    # get input/output filename
    
    arg.indir = arg.indir.rstrip('\\').rstrip('/')
    arg.outdir = arg.outdir.rstrip('\\').rstrip('/')
    
    if not(arg.indir or arg.inf) :
        raise ValueError("No useable input file address")
    if (arg.indir == '') and (not(os.path.exists(arg.inf))) :
        arg.indir = 'E:\MDNotes\Word\RawWords' 
    if arg.indir == '' and os.path.exists(arg.inf): 
        InputFileName = arg.inf
    elif os.path.exists(arg.inf):
        InputFileName = '\\'.join((arg.indir, arg.inf))
    else :
        raise ValueError('InputFile does not exist')
    
    if not(arg.outdir or arg.outf) :
        OutputFileName = setOutputFileName(InputFileName,arg.outp)
    else :
        OutputFileName = '\\'.join((arg.outdir, arg.outf))
    OutputFileName = OutputFileName.lstrip('\\')
    # print(OutputFileName)
    return SortMode, InputPhase, OutputPhase, InputFileName, OutputFileName


def main() : 
    SortMode, InputPhase, OutputPhase, InputFileName, OutputFileName = ProcessParas()
    print(SortMode)
    

    # assert 1==0
    # InputFileName = 'RawWords/Jimple生词.txt'
    # InputFileName = 'E:\MDNotes\Word&Trans\Words\MdWords\Jimple生词-Output.md'
    # InputPhase = 'M'
    # OutputPhase = 'Rn'

    # print(OutputFileName)
    # Check parameters
    # assert Phase.IsLegalInputPhase(InputPhase)
    # assert Phase.IsLegalOutputPhase(OutputPhase)
    #To be continued ...

    # 将文件内容转化成三元组
    if Phase.IsLegalRawInputPhase(InputPhase) : 
        FileTriad = RawFile2Triad(InputFileName)
    else :
        FileTriad = MDFile2Triad(InputFileName)

    FileTriad = SortFuncs[SortMode](FileTriad)

    if Phase.IsLegalMDOutputPhase(OutputPhase) : 
        Triad2MDFile(OutputFileName, FileTriad)
    else : 
        Triad2RawFile(OutputFileName, FileTriad)
    # Triad2MDFile(OutputFileName, FileTriad)

if __name__ == '__main__' : 
    main()
