class TV:

    canal = 1
    volumen = 1
    precio = 500
    _numTV = 0
    
    def __init__(self, marca, canal, precio, estado, volumen, control):
        self.marca = marca
        self.canal = int
        self.precio = int
        self.estado = bool
        self.volumen = int
        self.control = Control
        TV._TV__numTV +=1

    def __init__(self, marca, estado):
        self.estado = estado

    def setmarca(self, marca):
        self.marca = marca

    def setcontrol(self, control):
        self.control = Control

    def setprecio(self, precio):
        self.precio = precio

    def setvolumen(self, voulmen):
        self.volumen = volumen

    def setcanal(self, canal):
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
        self.canalUp = self.canal +1
        self.canalDown = self.canal -1
        
        if self.estado == True:
            if self.canalUp == True and self.canalUp <=120:
                self.canal = self.canalUp

            elif self.canalDown == True and self.canalDown >=1:
                self.canal = self.canalDown

    def cambiovolumen(self, volumen):
        self.volumenUp = self.volumen +1
        self.volumenDown = self.volumen -1
        
        if self.estado == True:
            if self.volumenUp == True and self.volumenUp <=7:
                self.volumen = self.volumenUp

            elif self.volumenDown == True and self.volumenDown >=0:
                self.volumen = self.volumenDown


