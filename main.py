import pyxel
from barril import barril
from escalera import escalera
from mario import mario
from plataforma import plataforma
from pauline import pauline
from donkey import donkey


class Game:

    def __init__(self):
        # set game running for sprites loading control
        self.gameRunning = False
        # final screen to control access to final screen sprites
        self.finalScreen = False
        # we define objects from various class to instance them
        # mario starts at 20, 230 coordinates and with 3 hp
        self.mario = mario(20, 232, 3)
        # the stairs will be settled as an object for control
        self.stairs = escalera()
        self.platform = plataforma()
        self.pauline = pauline(90, 35)
        self.donkey = donkey(24, 52)
        self.barrels = []
        # we create 10 barrel objects and store them in the barrels list
        while len(self.barrels) < 10:
            # all barrels start at 60, 70 coordinates
            self.barrels.append(barril(60, 74))
        # collide will be the control variable for mario being killed... or not
        self.collide = False
        self.hold = True
        # set map with 224x256 pyxels
        pyxel.init(224, 256)
        # load of sprites to the main window
        pyxel.load("sprites/mariod.pyxres")
        # load of backgrounds
        pyxel.image(1).load(0, 0, 'sprites/escenario.png')
        pyxel.image(2).load(0, 0, 'sprites/inicial.png')
        # now we launch the game
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # if mario gets to y=40 then game ended and happy day
        if self.mario.y == 40:
            # activate win protocol
            self.gameRunning = "win"

        # we use either marios hp>0 and game running as a control for the game updates and exiting the menu
        elif (pyxel.btnp(pyxel.KEY_SPACE) and not self.gameRunning) or (self.gameRunning and self.mario.vidas > 0):
            # start the game
            self.gameRunning = True

            # we need to control the kong launching barrels frequency by counting time with donkey
            if self.donkey.time == 30 or not self.hold:
                # hold is used to let mario have some time before the first barrel comes
                self.hold = False

                # if X is pressed you cannot be in a stair or already jumping for jumping protocol to be activated
                # else, will be ignored
                if pyxel.btn(pyxel.KEY_X) and not self.mario.OnJump and self.marioEscalera("comprobador") != "si":
                    # then we allow mario to jump and activate on jump protocol
                    self.mario.OnJump = True
                    # we settle max height for mario jump and declare mario in jump up protocol
                    # we will store the initial mario height for later check
                    self.mario.initial = self.mario.y
                    self.mario.OnJumpUp = True

                # W key will be allowed only on a stair coordinates and with jump or gravity (falling) disabled
                elif pyxel.btn(pyxel.KEY_W) and not self.mario.OnJump and not self.mario.gravity:
                    self.parameter_y("W")
                    # call Y function fo stair movement control
                    self.mario.moving = True
                    # true to help sprites control for animations

                # S key will be allowed only on a stair coordinates and with jump or gravity (falling) disabled
                elif pyxel.btn(pyxel.KEY_S) and not self.mario.OnJump and not self.mario.gravity:
                    self.parameter_y("S")
                    # call Y function fo stair movement control
                    self.mario.moving = True
                    # true to help sprites control for animations

                # if A key pressed and mario not in left border
                elif pyxel.btn(pyxel.KEY_A) and self.mario.x > -2:
                    self.parametroX("A")
                    # call X function to control standard mario movement protocol
                    self.mario.moving = True
                    # true to help sprites control for animations

                # if D key pressed and mario not in left border
                elif pyxel.btn(pyxel.KEY_D) and self.mario.x < 211:
                    self.parametroX("D")
                    # call X function to control standard mario movement protocol
                    self.mario.moving = True
                    # true to help sprites control for animations

                # if mario can't move or user didn't press any button
                else:
                    # need to calc if mario will stay still or fall because of gravity
                    if self.marioEscalera("comprobador") != "si" and not self.mario.OnJumpUp and (
                            self.marioPlataforma("D") == "cae" or self.marioPlataforma("A") == "cae"):
                        # let's fall down then
                        self.mario.y += 1
                        # gravity activated
                        self.mario.gravity = True

                    else:
                        # disable gravity because we are still as a rock
                        self.mario.gravity = False
                        # set mario moving to false for sprites control
                        self.mario.moving = False

                if self.mario.OnJumpUp:
                    # definition of jump protocol here
                    self.mario.gravity = True
                    # call to mario jump function
                    self.mario.mario_jump()

                elif self.mario.OnJump and (self.marioPlataforma("D") != "cae" or self.marioPlataforma("A") != "cae"):
                    self.mario.score_added = False
                    # este mario sumado es para el score ya que nos interesa que solo sume una vez por salto (no puede saltar dos barriles de golpe)
                    self.mario.OnJump = False
                    self.mario.gravity = False
                ######################aqui crearemos los barriles y sus funciones de movimiento#################################
            self.donkey.time = pyxel.frame_count % 100
            # aqui invocamos a los barriles y a la funcion de choque
            self.barrilPlataforma()
            self.choque_Barril_Mario()
        elif self.mario.vidas == 0:
            # si mario se queda sin vidas cargaremos la pantalla correspondiente
            self.gameRunning = "fin"

    def draw(self):
        pyxel.cls(0)
        if self.gameRunning == False:
            # pantalla para el inicio de juego
            pyxel.blt(0, 0, 2, 0, 0, 256, 256)
        elif self.gameRunning:
            # pantalla para el juego principal
            pyxel.blt(0, 0, 1, 0, 0, 256, 256)
            if self.hold == True and self.donkey.time >= 20 and self.donkey.time <= 30:
                pyxel.text(30, 220, "GO MARIO !!!", 7)
                # texto para indicar al jugador que ya puede salir!!
            ###################  evaluador de parametros en pantalla  ##########################
            pyxel.text(140, 10, "VIDAS DE MARIO :" + str(self.mario.vidas), 7)
            pyxel.text(140, 20, "SCORE DE MARIO :" + str(self.mario.score), 9)
            ###################  evaluador de parametros en pantalla  ##########################
            #############sprites de los barriles de alado de donkey kong##############
            pyxel.blt(2, 53, 0, 12, 103, 10, 16, colkey=0)
            pyxel.blt(2, 68, 0, 12, 103, 10, 16, colkey=0)
            pyxel.blt(12, 53, 0, 12, 103, 10, 16, colkey=0)
            pyxel.blt(12, 68, 0, 12, 103, 10, 16, colkey=0)
            ##############animaciones de pauline#################
            self.pauline.grito = pyxel.frame_count % 200
            self.pauline.frec = pyxel.frame_count % 6
            self.pauline.gritoPauline()
            if self.pauline.procesoGrito == True:
                pyxel.blt(115, 30, 0, 125, 182, 25, 7, colkey=0)
            # mensaje help
            pyxel.blt(self.pauline.x, self.pauline.y, 0, self.pauline.spx, 179, 15, 21, colkey=0)
            ###########################animaciones de mario###################
            self.spritesMario()
            self.mario.aniMario()
            self.mario.time = pyxel.frame_count % 10
            pyxel.blt(self.mario.x, self.mario.y, 0, self.mario.spX, self.mario.spY, (self.mario.spDir) * 16, 16,
                      colkey=0)
            ##############animaciones de la lista de barriles#############
            for elemento in self.barrels:
                # si el elemento de la lista está en movimiento,ejecutará uno u otro dependiendo de si escalera es true o no
                elemento.time = pyxel.frame_count % 12
                if elemento.moving and elemento.bajarEscalera == False:
                    elemento.aniBarril()
                    # uso variables para darle el valor que necesito a los sprites, desde direccion a un nuevo sprite
                    pyxel.blt(elemento.x, elemento.y, 0, 35, 106, (elemento.spDx) * 12, (elemento.spDy) * 10, colkey=0)
                elif elemento.bajarEscalera and elemento.moving:
                    elemento.aniBarril()
                    # esta es la animacion cuando está bajando una escalera locooo
                    pyxel.blt(elemento.x, elemento.y, 0, elemento.spTx, elemento.spTy, 16, 10, colkey=0)
            #################animaciones del oil y el fuego de encima#############
            if pyxel.frame_count % 10 < 5:
                pyxel.blt(2, 216, 0, 24, 0, 15, 16, colkey=0)
            else:
                pyxel.blt(2, 216, 0, 40, 0, 15, 16, colkey=0)
            pyxel.blt(0, 232, 0, 8, 0, 16, 16, colkey=0)
            ###############animaciones de donkey kong##############
            if self.donkey.time >= 35 and self.donkey.time <= 55:
                # si dk esta en ese tiempo está en posicion de coger barril en la segunda (elif) cuando lo suelta
                pyxel.blt(self.donkey.x, self.donkey.y, 0, 53, 58, 42, 32, colkey=0)
            elif self.donkey.time >= 20 and self.donkey.time <= 30:
                pyxel.blt(60, 74, 0, 35, 106, 12, 10, colkey=0)
                pyxel.blt(self.donkey.x, self.donkey.y, 0, 53, 58, -42, 32, colkey=0)
            else:
                # siempre que no coja o suelte barril tendrá un barril en sus manos preparado para soltarlo
                pyxel.blt(self.donkey.x, self.donkey.y, 0, 8, 213, 42, 32, colkey=0)
        ###############################################
        elif self.gameRunning == "fin":
            pyxel.cls(0)
            # si se ha acabado el juego por derrota a mario creamos la pantalla de lost
            pyxel.text(20, 125, "ENHORABUENA LA HAS LIADO TO PARDA Y HAS PERDIDO XD ", 9)
            pyxel.text(20, 145, "PULSA Q PARA ACABAR TU AVENTURA", 9)
            pyxel.text(80, 40, "PERDISTE SIMPLE HUMANO,HA HA HA...", 9)
            if pyxel.frame_count % 10 < 5:
                pyxel.blt(50, 50, 0, 150, 58, -50, 40, colkey=0)
            else:
                pyxel.blt(50, 50, 0, 150, 58, 50, 40, colkey=0)

        ###############################################    
        elif self.gameRunning == "win":
            pyxel.cls(0)
            # si se ha acabado el juego por derrota a donkey kong creamos la pantalla de lost
            pyxel.blt(50, 50, 0, 54, 179, 15, 21, colkey=0)
            pyxel.blt(70, 45, 0, 191, 180, 20, 20, colkey=0)
            pyxel.text(20, 125, "GENIAL AVENTURERO, LA HAS RESCATADO!!!!", 9)
            pyxel.text(20, 145, "PULSA Q PARA ACABAR TU AVENTURA", 9)

    ######################################################################################################################
    def spritesMario(self):
        # funcion para saber que sprite usar. En la clase mario es donde los invocamos para usarlo en el draw
        if self.mario.OnJump or self.mario.gravity:
            self.mario.dir = "aire"
            return "aire"
        # si está en aire o escalera retorna eso y si no retorna un suelo
        elif self.marioEscalera("comprobador"):
            self.mario.dir = "escalera"
            return "escalera"
        else:
            self.mario.dir = "suelo"
            return "suelo"

    def choque_Barril_Mario(self):
        collide = None
        # comparamos toda la lista de objetos barril si alguno coincide con mario en cierto intervalo en x e y
        for Barril in self.barrels:
            if Barril.moving == True:
                if self.mario.x >= Barril.x - 13 and self.mario.x <= Barril.x + 9:
                    if self.mario.y <= Barril.y + 7 and self.mario.y >= Barril.y - 13:
                        collide = True
                    # aprovechamos este metodo para saber si mario se ha situado sobre un barril (solo si está saltando, obviamente)
                    elif self.mario.OnJump and self.mario.y <= Barril.y - 13 and self.mario.y >= Barril.y - 18 and self.mario.score_added == False:
                        self.mario.scoreCalc()

        if collide:
            # si ha colisionado con mario, cancelaremos todos los movimientos de ambos
            # al hacerlo les forzaremos a respawnear en sus posiciones iniciales a todos los barriles y a mario
            self.mario.OnJump = False
            self.mario.OnJumpUp = False
            self.mario.x = 20
            self.mario.y = 232
            self.mario.moving = False
            # we need to reset mario animation to standard right
            self.mario.vidas -= 1
            self.colision = True
            self.hold = True
            # decimos que quieto sea true para volver a darle tiempo a barriles salir y que la anterior accion de mario no moleste con el respwan
            for Barril in self.barrels:
                Barril.moving = False
                Barril.x = 60
                Barril.y = 74

    ######################################################################################################################
    def parameter_y(self, direccion):
        if direccion == "W":
            # funcion para invocar la funcion escalera pero que no corrompa las animaciones (da muchos bugs si no)
            if self.marioEscalera(direccion) == "sube":
                self.mario.y -= 1
        elif direccion == "S":
            if self.marioEscalera(direccion) == "baja":
                self.mario.y += 1

    def marioEscalera(self, direccion):
        # aqui comprobaremos la direccion que nos dan y si es W o S buscaremos en el objeto escalera si alguna coincide
        # si coincide devolveremos un quieto o sube dependiendo de su posicion (si está al final de la escalera: "quieto")
        if direccion == "W":
            for elemento in self.stairs.escaleraMario:
                if self.mario.x >= elemento[0] and self.mario.x <= elemento[1] and self.mario.y <= elemento[
                    2] and self.mario.y > elemento[3]:
                    if self.mario.y == elemento[3]:
                        return "quieto"
                    else:
                        return "sube"
        elif direccion == "S":
            for elemento in self.stairs.escaleraMario:
                if self.mario.x >= elemento[0] and self.mario.x <= elemento[1] and self.mario.y < elemento[
                    2] and self.mario.y >= elemento[3]:
                    return "baja"
        # este elif es el de comprobador, lo usaremos para las distintas animaciones que vamos a usar durante el juego de mario
        elif direccion == "comprobador":
            for elemento in self.stairs.escaleraMario:
                if self.mario.x >= elemento[0] and self.mario.x <= elemento[1] and self.mario.y < elemento[
                    2] - 1 and self.mario.y > elemento[3]:
                    if self.mario.OnJump == True:
                        return False
                    else:
                        return "si"

    def parametroX(self, direccion):
        # este funciona de la misma manera que el parametro y solo que aqui hay dos nuevas: puede caer o puede subir tambien
        # funcion para invocar la funcion movimiento en plataforma pero que no corrompa las animaciones (da muchos bugs si no)
        if direccion == "A" and (self.marioEscalera("comprobador") != True or self.mario.OnJump == True):
            self.mario.spDir = 1
            # spdir esta para saber en que direccion debe ir la animacion de mario y mario saltando
            if self.marioPlataforma(direccion) == "avanza":
                self.mario.x -= 1
            elif self.marioPlataforma(direccion) == "sube":
                self.mario.y -= 1
                self.mario.x -= 1
            elif self.marioPlataforma(direccion) == "cae" and not self.mario.OnJumpUp:
                self.mario.y += 1
                self.mario.x -= 1
            elif self.marioPlataforma(direccion) == "cae" and self.mario.OnJumpUp:
                self.mario.x -= 1
        elif direccion == "D" and self.marioEscalera("comprobador") != True:
            self.mario.spDir = -1
            # spdir esta para saber en que direccion debe ir la animacion de mario y mario saltando (-1 para girarla vaya xd)
            if self.marioPlataforma(direccion) == "avanza":
                self.mario.x += 1
            elif self.marioPlataforma(direccion) == "sube":
                self.mario.y -= 1
                self.mario.x += 1
            elif self.marioPlataforma(direccion) == "cae" and not self.mario.OnJumpUp:
                self.mario.y += 1
                self.mario.x += 1
            elif self.marioPlataforma(direccion) == "cae" and self.mario.OnJumpUp:
                self.mario.x += 1

    def marioPlataforma(self, direccion):
        # si al calcular aqui su posicion usando el objeto plataformaMario para ello, comprobamos que
        # no está sobre ninguna, caerá. en caso de encontrarse justo al final de un peldaño subirá uno en y
        move = None
        for intervalo in self.platform.listaMario:
            if self.mario.x >= intervalo[0] and self.mario.x <= intervalo[1] and self.mario.y == intervalo[2]:
                if intervalo[3] == 1 or intervalo[3] == 3 or intervalo[3] == 5:
                    if self.mario.x == intervalo[1] and direccion == "D":
                        move = "sube"
                    else:
                        move = "avanza"
                elif intervalo[3] == 2 or intervalo[3] == 4 or intervalo[3] == 6:
                    if self.mario.x == intervalo[0] and direccion == "A":
                        move = "sube"
                    else:
                        move = "avanza"
        if move == "avanza":
            return "avanza"
        elif move == "sube":
            return "sube"
        else:
            return "cae"

    ######################################################################################################################
    def barrilPlataforma(self):
        # aqui buscamos un barril que no esté en movimiento y lo empezamos a mover
        lanzado = False
        if self.donkey.time == 30:
            # primer bucle para dotar de movimiento o no a un barril
            for Barril in self.barrels:
                if Barril.moving == False and lanzado == False:
                    Barril.moving = True
                    lanzado = True

        for Barril in self.barrels:
            # second loop for barrel movement selection
            movimiento = None
            if Barril.moving and Barril.x >= 3:
                import random
                for intervalo in self.stairs.barril:
                    if Barril.x >= intervalo[0] and Barril.x <= intervalo[1] and Barril.y == intervalo[2]:
                        if random.randint(1, 4) == 1:
                            Barril.bajarEscalera = True
                        else:
                            Barril.bajarEscalera = False
                # si el barril esta en bajarescalera, le haremos bajar en y hasta que se cumpla algo del for de abajo
                if Barril.bajarEscalera == True:
                    Barril.y += 1
                # buscamos en la lista de objetos plataforma si alguno coincide
                # primero determinamos en que cuadrante del mapa para saber su direccion
                # cuadrante guardado entre comillas en la clase barril
                for intervalo in self.platform.listaMario:
                    if intervalo[3] == 1 or intervalo[3] == 3 or intervalo[3] == 5:
                        if Barril.x >= intervalo[0] + 4 and Barril.x <= intervalo[1] + 4 and Barril.y == intervalo[
                            2] + 6:
                            movimiento = "move"
                            direccion = "A"

                    elif intervalo[3] == 2 or intervalo[3] == 4 or intervalo[3] == 6:
                        if Barril.x >= intervalo[0] - 1 and Barril.x <= intervalo[1] - 1 and Barril.y == intervalo[
                            2] + 6:
                            movimiento = "move"
                            direccion = "D"

                if movimiento == "move" and direccion == "A":
                    Barril.x -= 2.8
                    Barril.bajarEscalera = False

                elif movimiento == "move" and direccion == "D":
                    Barril.x += 2.8
                    Barril.bajarEscalera = False
                # aqui nos aseguramos de que el barril no baje doble solo xq está en caida de escalera jeje
                elif Barril.bajarEscalera == False:
                    Barril.y += 1

            else:
                Barril.moving = False
                Barril.x = 60
                Barril.y = 74
    ######################################################################################################################


Game()
