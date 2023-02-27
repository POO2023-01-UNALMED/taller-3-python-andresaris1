class TV:

    canal = 1
    volumen = 1
    precio = 500
    _numTV = 0
    
    def __init__(self, marca, canal, precio, estado, volumen, control):
        self.marca = marca
        self.canal = canal
        self.precio = precio
        self.estado = estado
        self.volumen = volumen
        self.control = control


    def TV(self, marca, estado):
        self.estado = estado

    def setmarca(self, marca):
        self.marca = marca

    def setcontrol(self, control):
        self.control = control

    def setprecio(self, precio):
        self.precio = precio

    def setvolumen(self, voulmen):
        self.volumen = volumen

    def setcanal(self, canal):
        if canal<=120 or canal>=1:
            self.canal = canal

    def getmarca(self):
        return self.marca

    def getcontrol(self):
        return self.control

    def getprecio(self):
        return self.precio

    def getvolumen(self):
        return self.volumen

    def getcanal(self):
        return self.canal

    def turn(self, turnOn, turnOff):
        if self.turnOn == True:
            self.estado = True
        
        elif self.turnOff == True:
            self.estado = False
        
    def getestado(self):
        if self.estado == True:
            self.estado = 'encendido'
        else:
            self.estado = 'no encendido'

    def cambiocanal(self, canal):
        canalUp = self.canal +1
        canalDown = self.canal -1
        
        if self.estado == True:
            if canalUp == True and canalUp <=120:
                self.canal = self.canalUp

            elif canalDown == True and canalDown >=1:
                self.canal = canalDown

    def cambiovolumen(self, volumen):
        volumenUp = self.volumen +1
        volumenDown = self.volumen -1
        
        if self.estado == True:
            if volumenUp == True and volumenUp <=7:
                self.volumen = volumenUp

            elif self.volumenDown == True and volumenDown >=0:
                self.volumen = volumenDown

    @classmethod
    def setnumTV(cls):
        cls._numTV +=1
    @classmethod
    def getnumTV(cls):
        return numTV

