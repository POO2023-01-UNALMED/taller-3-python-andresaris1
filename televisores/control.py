class Control:
    def __init__(self):
        self.tv = None

    def setTV(self, tv):
        self.tv = tv

    def getTV(self):
        return self.tv

    def turnOn(self):
        if self.tv:
            self.tv.turnOn()

    def turnOff(self):
        if self.tv:
            self.tv.turnOff()

    def canalUp(self):
        if self.tv:
            self.tv.canalUp()

    def canalDown(self):
        if self.tv:
            self.tv.canalDown()

    def volumenUp(self):
        if self.tv:
            self.tv.volumenUp()

    def volumenDown(self):
        if self.tv:
            self.tv.volumenDown()

    def setCanal(self):
        self.tv.setCanal()

    def enlazar(self, tv):
        self.tv = tv
        tv.setControl(self)
