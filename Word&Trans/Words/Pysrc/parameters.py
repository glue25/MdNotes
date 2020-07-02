
ELEMENTS_NUM = 3
IMPORTANCE = ['*','=','']


# Define Legal Phases.
class Phase() :
    _Phases = {}
    _Phases['LegalRawInputPhase'] = ['R', 'Rc', 'Rn', 'Rws']
    _Phases['LegalRawInputPhase'] = _Phases['LegalRawInputPhase'] + [x.lower() for x in _Phases['LegalRawInputPhase']]
    _Phases['LegalMDInputPhase'] = [x.replace('R', 'M') for x in _Phases['LegalRawInputPhase']]
    _Phases['LegalInputPhase'] = _Phases['LegalRawInputPhase'] + _Phases['LegalMDInputPhase']
    _Phases['LegalRawOutputPhase'] = ['Rc', 'Rn', 'Rws']
    _Phases['LegalRawOutputPhase'] = _Phases['LegalRawOutputPhase'] + [x.lower() for x in _Phases['LegalRawOutputPhase']]
    _Phases['LegalMDOutputPhase'] = [x.replace('R', 'M') for x in _Phases['LegalRawOutputPhase']]
    _Phases['LegalOutputPhase'] = _Phases['LegalRawOutputPhase'] + _Phases['LegalMDOutputPhase'] 
    LegalInputPhase = _Phases['LegalRawInputPhase'] + _Phases['LegalMDInputPhase']
    LegalOutputPhase = _Phases['LegalRawOutputPhase'] + _Phases['LegalMDOutputPhase'] 
    
    LegalSortMod = ['character', 'importance', 'ignore']
    

    @staticmethod
    def IsLegalInputPhase(phase) :
        return phase in Phase.LegalSortMod

    @staticmethod
    def IsLegalInputPhase(phase) :
        return phase in Phase._Phases['LegalInputPhase']

    @staticmethod
    def IsLegalOutputPhase(phase) :
        return phase in Phase._Phases['LegalOutputPhase']

    @staticmethod
    def IsLegalRawInputPhase(phase) :
        return phase in Phase._Phases['LegalRawInputPhase']

    @staticmethod
    def IsLegalMDInputPhase(phase) :
        return phase in Phase._Phases['LegalMDInputPhase']

    @staticmethod
    def IsLegalRawOutputPhase(phase) :
        return phase in Phase._Phases['LegalRawOutputPhase']

    @staticmethod
    def IsLegalMDOutputPhase(phase) :
        return phase in Phase._Phases['LegalMDOutputPhase']

