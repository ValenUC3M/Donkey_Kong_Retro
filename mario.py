


class mario:
    
    
    def __init__(self,x,y,vidas):
        self.x = x
        self.y = y
        self.vidas = vidas
        self.inicial = None
        self.procesoSalto = False
        self.procesoSaltoUp = False
        self.gravedad = False
        self.spX = 5
        self.spY = 32
        self.spDir = -1
        self.dir = "suelo"
        self.moving = False
        #score y sumado son para el score de mario
        self.score = 0
        self.sumado = False
        #variable de mario para las vidas , salto, las animaciones (sps, dir y moving)
    
    
    #aqui calcularemos el valor del score de mario si salta un barril   
    def scoreCalc(self):
        if self.sumado == False:
            self.score += 100
            self.sumado = True
    #funcion de salto de mario que hace que suba hasta cierta Y, y luego baja usando la gravedad del main        
    def saltoMario(self):
        if self.procesoSaltoUp == True:
            self.y -= 1.5
            if self.inicial-15 == self.y:
                self.procesoSaltoUp = False
            elif self.inicial == self.y:
                self.procesoSalto = False
    #aqui tenemos las diferentes animaciones que mario podrá usar del pyxeleditor
    #definimos la posicion de donde debe cogerla usando spX y spY            
    def aniMario(self):
        if self.dir == "aire":
            self.spX =221
            self.spY =32
        elif self.dir == "escalera":
            self.spX =77
            self.spY =32
            if self.moving:
                if self.time < 5:
                    self.spDir = -1
                elif self.time >= 5:
                    self.spDir = 1
            else:
                self.spDir = +1
               
        elif self.dir == "suelo":
            if self.moving:
                if self.time < 5:
                    self.spX =5
                    self.spY =32
                elif self.time >= 5:
                    self.spX =28
                    self.spY =32
            else:
                self.spX =5
                self.spY =32
                
        elif self.dir == "sueloStop":
            self.spX =5
            self.spY =32
        elif self.dir == "escaleraStop":
            self.spX =5
            self.spY =32
            
            
        
        
        
    
    '''@property
    def x(self):
        return self.__x
    @x.setter
    def x(self,v):
        self.__x = v
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,w):
        self.__y = w
    @property
    def d(self):
        return self.__d'''
    
    