class JugState:
    capacity = 0               #defining variables
    currentVol = 0
    name = 'new jug'

    def __init__(self, capacity, name):     #initiating function
        self.capacity = capacity
        self.name = name
        self.currentVol = 0

    def fill(self):                         #Filling function
        self.currentVol = self.capacity

    def is_full(self):                      #Checking currnt vol to full
        return self.currentVol == self.capacity

    def is_empty(self):                     #Checking currnt vol to empty
        return self.currentVol == 0

    def dump(self):                         #removing volume in the jug
        self.currentVol = 0

    def transfer(self, target_jug):         #Transfer function

        targetVol = min(target_jug.capacity,
                            (target_jug.currentVol + self.currentVol))
        
        self_volume = max(0, target_jug.currentVol +
                       self.currentVol - target_jug.capacity)
        
        self.currentVol = self_volume
        target_jug.currentVol = targetVol

        return True

