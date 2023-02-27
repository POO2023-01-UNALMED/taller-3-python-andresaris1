class Control:
    def __init__(self, tv, turnOn, turnOff, canalUp, canalDown, volumenUp, volumenDown, setCanal, enlazar):
        self.tv = tv
        self.turnOn = bool
        self.turnOff = bool
        self.canalUp = int
        self.canalDown = int
        self.volumenUp = int
        self.volumenDown = int
        self.setCanal = int
        self.enlazar = str

    def setenlazar(self, televisor):
        self._enlazar = televisor

    def getenlazar(self):
        if(isinstance(self._enlazar, TV)):
            self._enlazar
