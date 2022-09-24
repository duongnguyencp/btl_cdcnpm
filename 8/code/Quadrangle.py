
class Quadrangle:
    def __init__(self):
        print("")
    def getQuad(self):
        allQuad=[]
        quad = "MC-01: Mare Boreum (North Pole)"
        allQuad.append(quad)
        quad = "MC-02: Diacria"
        allQuad.append(quad)
        quad = "MC-03: Arcadia"
        allQuad.append(quad)
        quad = "MC-04: Mare Acidalium"
        allQuad.append(quad)
        quad = "MC-05: Ismenius Lacus"
        allQuad.append(quad)
        quad = "MC-06: Casius"
        allQuad.append(quad)
        quad = "MC-07: Cebrenia"
        allQuad.append(quad)
        quad = "MC-08: Amazonis"
        allQuad.append(quad)
        quad = "MC-09: Tharsis"
        allQuad.append(quad)
        quad = "MC-10: Lunae Palus"
        allQuad.append(quad)
        quad = "MC-11: Oxia Palus"
        allQuad.append(quad)
        quad = "MC-12: Arabia"
        allQuad.append(quad)
        quad = "MC-13: Syrtis Major"
        allQuad.append(quad)
        quad = "MC-14: Amenthes"
        allQuad.append(quad)
        quad = "MC-15: Elysium"
        allQuad.append(quad)
        quad = "MC-16: Memnonia"
        allQuad.append(quad)
        quad = "MC-17: Phoenicis Lacus"
        allQuad.append(quad)
        quad = "MC-18: Coprates"
        allQuad.append(quad)
        quad = "MC-19: Margaritifer Sinus"
        allQuad.append(quad)
        quad = "MC-20: Sinus Sabaeus"
        allQuad.append(quad)
        quad = "MC-21: Iapygia"
        allQuad.append(quad)
        quad = "MC-22: Mare Tyrrhenum"
        allQuad.append(quad)
        quad = "MC-23: Aeolis"
        allQuad.append(quad)
        quad = "MC-24: Phaethontis"
        allQuad.append(quad)
        quad = "MC-25: Thaumasia"
        allQuad.append(quad)
        quad = "MC-26: Argyre"
        allQuad.append(quad)
        quad = "MC-27: Noachis"
        allQuad.append(quad)
        quad = "MC-28: Hellas"
        allQuad.append(quad)
        quad = "MC-29: Eridania"
        allQuad.append(quad)
        quad = "MC-30: Mare Australe (South Pole)"
        allQuad.append(quad)
        return allQuad
    def toQuad(self,LATITUDE_CIRCLE_IMAGE, LONGITUDE_CIRCLE_IMAGE):
        LA = LATITUDE_CIRCLE_IMAGE
        LO = LONGITUDE_CIRCLE_IMAGE + 180
        if LA >=  65 and LA <=  90 and LO >=   0 and LO <= 360 : 
            quad = "MC-01: Mare Boreum (North Pole)"
        elif LA >=  30 and LA <   65 and LO >= 120 and LO <  180 : 
            quad = "MC-02: Diacria"
        elif LA >=  30 and LA <   65 and LO >=  60 and LO <  120 : 
            quad = "MC-03: Arcadia"
        elif LA >=  30 and LA <   65 and LO >=   0 and LO <   60 : 
            quad = "MC-04: Mare Acidalium"
        elif LA >=  30 and LA <   65 and LO >= 300 and LO <= 360 : 
            quad = "MC-05: Ismenius Lacus"
        elif LA >=  30 and LA <   65 and LO >= 240 and LO <  300 : 
            quad = "MC-06: Casius"
        elif LA >=  30 and LA <   65 and LO >= 180 and LO <  240 : 
            quad = "MC-07: Cebrenia"
        elif LA >=   0 and LA <   30 and LO >= 135 and LO <  180 : 
            quad = "MC-08: Amazonis"
        elif LA >=   0 and LA <   30 and LO >=  90 and LO <  135 : 
            quad = "MC-09: Tharsis"
        elif LA >=   0 and LA <   30 and LO >=  45 and LO <   90 : 
            quad = "MC-10: Lunae Palus"
        elif LA >=   0 and LA <   30 and LO >=   0 and LO <   45 : 
            quad = "MC-11: Oxia Palus"
        elif LA >=   0 and LA <   30 and LO >= 315 and LO <= 360 : 
            quad = "MC-12: Arabia"
        elif LA >=   0 and LA <   30 and LO >= 270 and LO <  315 : 
            quad = "MC-13: Syrtis Major"
        elif LA >=   0 and LA <   30 and LO >= 225 and LO <  270 : 
            quad = "MC-14: Amenthes"
        elif LA >=   0 and LA <   30 and LO >= 180 and LO <  225 : 
            quad = "MC-15: Elysium"
        elif LA >= -30 and LA <    0 and LO >= 135 and LO <  180 : 
            quad = "MC-16: Memnonia"
        elif LA >= -30 and LA <    0 and LO >=  90 and LO <  135 : 
            quad = "MC-17: Phoenicis Lacus"
        elif LA >= -30 and LA <    0 and LO >=  45 and LO <   90 : 
            quad = "MC-18: Coprates"
        elif LA >= -30 and LA <    0 and LO >=   0 and LO <   45 : 
            quad = "MC-19: Margaritifer Sinus"
        elif LA >= -30 and LA <    0 and LO >= 315 and LO <= 360 : 
            quad = "MC-20: Sinus Sabaeus"
        elif LA >= -30 and LA <    0 and LO >= 270 and LO <  315 : 
            quad = "MC-21: Iapygia"
        elif LA >= -30 and LA <    0 and LO >= 225 and LO <  270 : 
            quad = "MC-22: Mare Tyrrhenum"
        elif LA >= -30 and LA <    0 and LO >= 180 and LO <  225 : 
            quad = "MC-23: Aeolis"
        elif LA >= -65 and LA <  -30 and LO >= 120 and LO <  180 : 
            quad = "MC-24: Phaethontis"
        elif LA >= -65 and LA <  -30 and LO >=  60 and LO <  120 : 
            quad = "MC-25: Thaumasia"
        elif LA >= -65 and LA <  -30 and LO >=   0 and LO <   60 : 
            quad = "MC-26: Argyre"
        elif LA >= -65 and LA <  -30 and LO >= 300 and LO <= 360 : 
            quad = "MC-27: Noachis"
        elif LA >= -65 and LA <  -30 and LO >= 240 and LO <  300 : 
            quad = "MC-28: Hellas"
        elif LA >= -65 and LA <  -30 and LO >= 180 and LO <  240 : 
            quad = "MC-29: Eridania"
        elif LA >= -90 and LA <  -65 and LO >=   0 and LO <= 360 : 
            quad = "MC-30: Mare Australe (South Pole)"
        return quad
