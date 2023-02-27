class TV:

    canal = 1
    volumen = 1
    precio = 500
    numTV = 0
    

    @classmethod
    def setNumTV(cls, numTV):
        cls.numTV = numTV

    @classmethod
    def getNumTV(cls):
        return numTV
    

    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.control= None
        

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_canal(self):
        return self.canal

    def set_canal(self, canal):
        if self.estado and 1 <= canal <= 120:
            self.canal = canal

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def get_estado(self):
        return self.estado

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def canalUp(self):
        if self.estado and self.canal < 120:
            self.canal += 1

    def canalDown(self):
        if self.estado and self.canal > 1:
            self.canal -= 1

    def volumenUp(self):
        if self.estado and self.volumen < 7:
            self.volumen += 1

    def volumenDown(self):
        if self.estado and self.volumen > 0:
            self.volumen -= 1

    def get_volumen(self):
        return self.volumen

    def set_volumen(self, volumen):
        if self.estado and 0 <= volumen <= 7:
            self.volumen = volumen

    def get_control(self):
        return self.control

    def set_control(self, control):
        self.control = control
