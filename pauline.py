


class pauline:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.grito = None
        self.frec = None
        self.procesoGrito = False
        self.spx = 54
        #tenemos ñas variable de pauline solo para animaciones y su x y su Y un poco por decorar la verdad
        
    def gritoPauline(self):
        #si cumple que está en proceso grito ejecutará los sprites de agitarse fuertemente, si no pauline está quieta
        if self.grito == 150:
            self.procesoGrito = True
        if self.procesoGrito == True and self.grito >= 150 and self.grito <= 190:
            if self.frec <= 3:
                self.spx = 30
            elif self.frec > 3:
                self.spx = 6 
        else:
            self.procesoGrito = False
            self.spx = 54
            
            
            
            
            
        
        
        
        

