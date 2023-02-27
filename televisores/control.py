class Control:
    def __init__(self, tv):
        self._tv = None

    def get_tv(self):
        return self._tv
    def set_tv(self):
        self._tv = tv

    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalDown

    def volumenUp(self):
        self._tv.volumenUp
    def volumenDown(self):
        self._tv.volumenDown

    def turnOn(self):
        self._tv.turnOn
    def turnOff(self):
        self._tv.turnOff

    def setCanal(self):
        self._tv.sercanal
        

    def enlazar(self, tv):
        self._tv = tv
        self._tv-setcontrol(self)


