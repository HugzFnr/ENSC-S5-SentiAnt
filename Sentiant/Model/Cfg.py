class Cfg:
    def __init__(self):
        pass

    HPMAX = 2
    FOV=7
    HPRADIUS = 5
    WIDTH=42
    HEIGHT=42

    UP = {x: 0, y: -1}
    DOWN = {x: 0, y: 1}
    RIGHT = {x: 1, y: 0}
    LEFT = {x: -1, y:0}

    MOVE = "move"
    DIG = "dig"
    DROP = "drop"
    PICKUP = "pickup"
    ATTACK = "attack"
    SLEEP = "sleep"
    PHERO = "phero" # Attention à ne pas faire phero sur un rocher mdr

    NULL = "null"



