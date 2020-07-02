from operator import itemgetter, indexOf
from functools import partial

from Pysrc.parameters import *

Mods = Phase.LegalSortMod


def SortbyCharacter(TriadGenerator) :
    return iter(sorted(TriadGenerator,key=itemgetter(0)))
def SortbyImportance(TriadGenerator) :
    def func(x) :
        return indexOf(IMPORTANCE,itemgetter(ELEMENTS_NUM-1)(x))
    return iter(sorted(TriadGenerator,key=func))


SortFuncs = {
    'character' : SortbyCharacter, 
    'importance': SortbyImportance,
    'ignore' : lambda x:x
}
assert list(SortFuncs.keys()) == Mods





