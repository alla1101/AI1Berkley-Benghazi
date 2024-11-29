# init Parameters
costGraph = {
    "AB":1,
    "AC":4,
    "BC":1,
    "BT":1,
    "BK":1,
    "CT":2,
    "CK":3,
    "TK":1,
    "TD":3,
    "KD":1,
    "DE":8,
    "DF":3,
    "DG":9,
    "EG":2,
    "FG":5
}
startingPoint="A"
goalPoint="G"
maxFoundInput=90
def heuristicAlla(state,problem):
    x={
        "A":11,
        "B":10,
        "C":11,
        "T":10,
        "K":9,
        "D":8,
        "E":1,
        "F":7.5,
        "G":0
    }
    return x[state]
