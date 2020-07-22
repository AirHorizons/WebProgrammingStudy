scv = ['HP':60, 'ATK':5, 'DEF':1, 'DEFUPGRADE':2, 'move': lambda direction : 'position' + direction]
scv2 = []
scvlist = [scv, scv2]
for unitscv in scvlist:
    unitscv['DEFUPGRADE'] += 1

class Unit:
    def __init__(self):
        self.position = [0, 0]
    
    def move(self):
        pass
        # change position by its direction

class SCV(Unit):
    maxHP = 60
    ATK = 5
    DEF = 1
    DEFUPGRADE = 0

    def __init__(self):
        self.HP = SCV.maxHP
        self.type = 'player'

class Marine(unit):
    maxHP = 50
    ATK = 8
    DEF = 1
    DEFUPGRADE = 0

    def getATK():
        return Marine.ATK

marine = Marine()
marine.move('left')

marines = [Marine()]*100
