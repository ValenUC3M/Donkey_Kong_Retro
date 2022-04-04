class barril:
    
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.spTx = 0
        self.spTy = 0
        self.spDx = 0
        self.spDy = 0
        self.moving = False
        self.time = 0
        self.timeBajar = 0
        self.bajarEscalera = False
        #con los barriles es lo mismo que con mario, las sps sirven para las animaciones
        #en este caso en moving y el bajarescalera son para sus movimientos basicos
    
    def aniBarril(self):
        if self.bajarEscalera == True:
            if self.time < 3 or (self.time >= 6 and self.time < 9):
                self.spTx = 129
                self.spTy = 106
            else:
                self.spTx = 153
                self.spTy = 106
        #con respecto a mario está la diferencia de los cuadrantes
        #si el metodo cuadrante nos devuelve right el movimiento es hacia jupiter, no te fastidia xddd (es bromi)        
        if self.cuadrante() == "right":
            if self.time < 3:
                self.spDx = 1
                self.spDy = 1
            elif self.time >= 3 and self.time <6:
                self.spDx = -1
                self.spDy = 1
            elif self.time >= 6 and self.time <9:
                self.spDx = -1
                self.spDy = -1
            else:
                self.spDx = 1
                self.spDy = -1
        #si el metodo cuadrante no nos devuelve right el movimiento es hacia saturno,  (saturno se encuentra a la izquierda del mapa btw)    
        else:
            if self.time < 3:
                self.spDx = 1
                self.spDy = 1
            elif self.time >= 3 and self.time <6:
                self.spDx = 1
                self.spDy = -1
            elif self.time >= 6 and self.time <9:
                self.spDx = -1
                self.spDy = -1
            else:
                self.spDx = -1
                self.spDy = +1
        
        
    #si barril está entre ciertas Y devolveremos right o left para su direccion, aunq en realidad solo necesitariamos usar
    #la mitad de ellos (ya que usamos else en los sprites), pero es que me daba penita por las left :(   )    
    def cuadrante(self):
        if self.y <= 238 and self.y >= 231:
            return "left"
            #primer cuadrante
        elif self.y <= 230 and self.y >= 198:
            return "right"
            #segundo cuadrante
        elif self.y <= 197 and self.y >= 165:
            return "left"
            #tercero cuadrante
        elif self.y <= 164 and self.y >= 132:
            return "right"
            #cuarto cuadrante
        elif self.y <= 131 and self.y >= 99:
            return "left"
        elif self.y <= 98 and self.y >= 74:
            return "right"
            #quinto cuadrante'''
            

