import argparse

from Pysrc.parameters import Phase
from Pysrc.utilities import *

def process_args() :
    parser = argparse.ArgumentParser(description='Transform words.')
    parser.add_argument('-indir',help='input file dir')
    parser.add_argument('-inf', help='input file')
    parser.add_argument('-outdir', help='output file dir')
    parser.add_argument('-outf', help='output file')

    parser.add_argument('-inp', help='input phase', choices=Phase.LegalInputPhase)
    parser.add_argument('-outp', help='output phase', choices=Phase.LegalOutputPhase)
    args = parser.parse_args()
    return args



def main() : 
    arg = process_args()
    # print(arg.indir)
    InputFileName = 'RawWords/Jimple生词.txt'
    InputPhase = 'R'
    OutputPhase = 'Rn'

    OutputFileName = setOutputFileName(InputFileName,'Mc')
    print(OutputFileName)
    # Check parameters
    assert Phase.IsLegalInputPhase(InputPhase)
    assert Phase.IsLegalOutputPhase(OutputPhase)
    #To be continued ...

    #分单文件多文件情况处理，True对应单文件，条件慢慢补
    if True :
        # 将文件内容转化成三元组
        if Phase.IsLegalRawInputPhase(InputPhase) : 
            FileTriad = RawFile2Triad(InputFileName)
        else :
            FileTriad = MDFile2Triad(InputFileName)
    else :
        pass

    # print(FileTriad)
    # for i in FileTriad :
    #     print(i)
    
    Triad2MDFile(OutputFileName, FileTriad)

# filename = os.path.abspath(__file__)
# dir = os.path.split(filename)[0]
# dir += '\\RawWords'
# a = next(os.walk(dir))
# L = [a[0] + '\\' + x for x in a[2]]
# for i in L :
#     main2(i)
if __name__ == '__main__' : 
    main()

# def procss_args2(default_concur_req):
#     server_options = ', '.join(sorted(SERVERS))
#     parser = argparse.ArgumentParser(
#                 description='Transform words.')
#     parser.add_argument('-dir', metavar='CC', nargs='*',
#                 help='country code or 1st letter (eg. B for BA...BZ)')
#     parser.add_argument('-f', '--filename', action='store_true',
#                 help='get all available flags (AD to ZW)')
#     parser.add_argument('-e', '--every', action='store_true',
#                 help='get flags for every possible code (AA...ZZ)')
#     parser.add_argument('-l', '--limit', metavar='N', type=int,
#                 help='limit to N first codes', default=sys.maxsize)
#     parser.add_argument('-m', '--max_req', metavar='CONCURRENT', type=int,
#                 default=default_concur_req,
#                 help='maximum concurrent requests (default={})'
#                       .format(default_concur_req))
#     parser.add_argument('-s', '--server', metavar='LABEL',
#                 default=DEFAULT_SERVER,
#                 help='Server to hit; one of {} (default={})'
#                       .format(server_options, DEFAULT_SERVER))
#     parser.add_argument('-v', '--verbose', action='store_true',
#                 help='output detailed progress info')
#     args = parser.parse_args()
#     if args.max_req < 1:
#         print('*** Usage error: --max_req CONCURRENT must be >= 1')
#         parser.print_usage()
#         sys.exit(1)
#     if args.limit < 1:
#         print('*** Usage error: --limit N must be >= 1')
#         parser.print_usage()
#         sys.exit(1)
#     args.server = args.server.upper()
#     if args.server not in SERVERS:
#         print('*** Usage error: --server LABEL must be one of',
#               server_options)
#         parser.print_usage()
#         sys.exit(1)
#     try:
#         cc_list = expand_cc_args(args.every, args.all, args.cc, args.limit)
#     except ValueError as exc:
#         print(exc.args[0])
#         parser.print_usage()
#         sys.exit(1)

#     if not cc_list:
#         cc_list = sorted(POP20_CC)
#     return args, cc_list