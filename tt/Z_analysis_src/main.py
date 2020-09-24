
from utilities import find_str_from_file,find_str_from_files
from utilities import get_all_filenames
from utilities import Dirs

# L = find_str_from_files('DatalogProgram.h', None,show_row=False, useRE=False)
# for i in L :
#     print(i)

file_L = [
    'CompiledSouffle.h'
    'SouffleInterface.h'
    'gtirb.hpp'
]
L_gtirb = get_all_filenames(Dirs['gtirb'])
L_souffle = get_all_filenames(Dirs['souffle'])
L_dd = get_all_filenames(Dirs['Dir'])

Lt = []
for x in L_gtirb+L_souffle+L_dd : 
    for filename in file_L :
        if filename in x :
            Lt.append(x)

# Lt = [x if filename in x for x in L_gtirb+L_souffle for filename in file_L ]
print(Lt)


#include <souffle/CompiledSouffle.h>
#include <souffle/SouffleInterface.h>
#include <gtirb/gtirb.hpp>


# Fs = get_all_filenames(Dirs['gtirb'])
# for i in Fs :
#     print(i)
# print(len(Fs))
