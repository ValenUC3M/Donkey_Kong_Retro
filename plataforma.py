


class plataforma:
    
   def __init__(self):
      self.listaMario = [] 
      self.crearListaMario()
      
   '''basicamente lo que hacemos es crear el objeto escalera usando una lista de coordenadas donde estan todas las plataformas,
   se que no es objetos al 100% pero me parece más optimizado. En definitiva usamos esto para luego en marioplataforma comparar x e y''' 
   def crearListaMario(self):   
        #cuadrante uno en lista
       self.listaMario = [[-2,100,232,1]]
       x1 = 100
       x2 = 116
       y = 231
       while y >= 225:
           self.listaMario.append([x1,x2,y,1])
           x1 += 16
           x2 += 16
           y -= 1
    #################################################################   
    #cuadrante dos en lista
       self.listaMario.append([-2,13,192,2])
       x1 = 13
       x2 = 29
       y = 193
       while y <= 204:
           self.listaMario.append([x1,x2,y,2])
           x1 += 16
           x2 += 16
           y += 1
    #################################################################  
    #cuadrante tres en lista 
       x1 = 4
       x2 = 20
       y = 171
       while y >= 159:
           self.listaMario.append([x1,x2,y,3])
           x1 += 16
           x2 += 16
           y -= 1
    #################################################################
    #cuadrante cuatro en lista    
       self.listaMario.append([-2,13,126,4])
       x1 = 13
       x2 = 29
       y = 127
       while y <= 138:
           self.listaMario.append([x1,x2,y,4])
           x1 += 16
           x2 += 16
           y += 1
    #################################################################       
    #cuadrante cinco en lista 
       x1 = 4
       x2 = 20
       y = 105
       while y >= 93:
           self.listaMario.append([x1,x2,y,5])
           x1 += 16
           x2 += 16
           y -= 1
    #################################################################
    #cuadrante seis en listaMario
       self.listaMario.append([-2,141,68,6])
       x1 = 141
       x2 = 157
       y = 69
       while y <= 72:
           self.listaMario.append([x1,x2,y,6])
           x1 += 16
           x2 += 16
           y += 1
    #################################################################
    #cuadrante siete en listaMario
    #### plataforma en la que se encuentra la princesa ####
       self.listaMario.append([80,132,40,7])