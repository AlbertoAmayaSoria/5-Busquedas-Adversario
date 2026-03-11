"""
Modulo para las clases básicas para realizar un juego de forma muy simplificada
    
Vamos a usar una orientación funcional en este modulo

"""

from random import shuffle, choice
    
class JuegoZT2:
    """
    Clase abstracta para juegos de suma cero, por turnos, dos jugadores.
    
    Se asumen que los jugadores son 1 y -1
    
    """
    def inicializa(self):
        """
        Inicializa el estado inicial del juego, siempre inicia el jugador 1
        
        """
        t = tuple(80 * [0])
        t = t[:80] + (-2, -2)
        return t
        
        #raise NotImplementedError("Hay que desarrollar este método, pues")

    def jugadas_legales(self, s, j):
        """
        Devuelve una lista con las jugadas legales para el jugador j
        en el estado s

        """
        I_Arriba = {0, 1, 2, 
                    9, 10, 11,
                    18, 19, 20}
        I_Centro = {27, 28, 29, 
                    36, 37, 38, 
                    45, 46, 47}
        I_Abajo = {54, 55, 56,
                   63, 64, 65,
                   72, 73, 74}
        C_Arriba = {3, 4, 5,
                    12, 13, 14,
                    21, 22, 23}
        C_Centro = {30, 31, 32,
                    39, 40,41,
                    57, 58, 59}
        C_Abajo = {57, 58, 59,
                   66, 67, 68,
                   75, 76, 77}
        D_Arriba = {6, 7, 8,
                    15, 16, 17,
                    24, 25, 26}
        D_Centro = {33, 34, 35,
                    42, 43, 44,
                    51, 52, 53}
        D_Abajo = {60, 61, 62,
                   69, 70, 71,
                   78, 79, 80}
        #Jugador 1
        #No es eficiente
        if j > 0:
            if s[81] in I_Arriba:
                libres = [i for i in I_Arriba if s[i] == 0]
                if len(libres):
                    return libres
                else:
                    return [posicion for posicion in range(81) if s[posicion] == 0]
                
            elif s[81] in I_Centro:
                libres = [i for i in I_Centro if s[i] == 0]
                if len(libres):
                    return libres
                else:
                    return [posicion for posicion in range(81) if s[posicion] == 0]
            
            elif s[81] in I_Abajo:
                libres = [i for i in I_Abajo if s[i] == 0]
                if len(libres):
                    return libres
                else:
                    return [posicion for posicion in range(81) if s[posicion] == 0]
            
            elif s[81] in C_Arriba:
                libres = [i for i in C_Arriba if s[i] == 0]
                if len(libres):
                    return libres
                else:
                    return [posicion for posicion in range(81) if s[posicion] == 0]

            elif s[81] in C_Centro:
                libres = [i for i in C_Centro if s[i] == 0]
                if len(libres):
                    return libres
                else:
                    return [posicion for posicion in range(81) if s[posicion] == 0]

            elif s[81] in C_Abajo:
                libres = [i for i in C_Abajo if s[i] == 0]
                if len(libres):
                    return libres
                else:
                    return [posicion for posicion in range(81) if s[posicion] == 0]

            elif s[81] in D_Arriba:
                libres = [i for i in D_Arriba if s[i] == 0]
                if len(libres):
                    return libres
                else:
                    return [posicion for posicion in range(81) if s[posicion] == 0]

            elif s[81] in D_Centro:
                libres = [i for i in D_Centro if s[i] == 0]
                if len(libres):
                    return libres
                else:
                    return [posicion for posicion in range(81) if s[posicion] == 0]

            else: 
                s[81] in D_Abajo
                libres = [i for i in D_Abajo if s[i] == 0]
                if len(libres):
                    return libres
                else:
                    return [posicion for posicion in range(81) if s[posicion] == 0]

        #Jugador 2
        else:

            if s[82] in I_Arriba:
                libres = [i for i in I_Arriba if s[i] == 0]
                if len(libres):
                    return libres
                else:
                    return [posicion for posicion in range(81) if s[posicion] == 0]
                
            elif s[82] in I_Centro:
                libres = [i for i in I_Centro if s[i] == 0]
                if len(libres):
                    return libres
                else:
                    return [posicion for posicion in range(81) if s[posicion] == 0]
            
            elif s[82] in I_Abajo:
                libres = [i for i in I_Abajo if s[i] == 0]
                if len(libres):
                    return libres
                else:
                    return [posicion for posicion in range(81) if s[posicion] == 0]
            
            elif s[82] in C_Arriba:
                libres = [i for i in C_Arriba if s[i] == 0]
                if len(libres):
                    return libres
                else:
                    return [posicion for posicion in range(81) if s[posicion] == 0]

            elif s[82] in C_Centro:
                libres = [i for i in C_Centro if s[i] == 0]
                if len(libres):
                    return libres
                else:
                    return [posicion for posicion in range(81) if s[posicion] == 0]

            elif s[82] in C_Abajo:
                libres = [i for i in C_Abajo if s[i] == 0]
                if len(libres):
                    return libres
                else:
                    return [posicion for posicion in range(81) if s[posicion] == 0]

            elif s[82] in D_Arriba:
                libres = [i for i in D_Arriba if s[i] == 0]
                if len(libres):
                    return libres
                else:
                    return [posicion for posicion in range(81) if s[posicion] == 0]

            elif s[82] in D_Centro:
                libres = [i for i in D_Centro if s[i] == 0]
                if len(libres):
                    return libres
                else:
                    return [posicion for posicion in range(81) if s[posicion] == 0]

            else: 
                s[82] in D_Abajo
                libres = [i for i in D_Abajo if s[i] == 0]
                if len(libres):
                    return libres
                else:
                    return [posicion for posicion in range(81) if s[posicion] == 0]
            

        #raise NotImplementedError("Hay que desarrollar este método, pues")      
    
    def sucesor(self, s, a, j):
        """
        Devuelve el estado que resulta de realizar la jugada a en el estado s
        para el jugador j
        
        """
        raise NotImplementedError("Hay que desarrollar este método, pues")
    
    def terminal(self, s):
        """
        Devuelve True si es terminal el estado actual,
        
        """
        raise NotImplementedError("Hay que desarrollar este método, pues")
    
    def ganancia(self, s):
        """
        Devuelve la ganancia para el jugador 1 en el estado terminal s
        
        """
        raise NotImplementedError("Hay que desarrollar este método, pues")
    

class JuegoInterface:
    """
    Clase abstracta para mostrar el estado del juego, y pedir la jugada al usuario

    """
    def __init__(self, juego, jugador1, jugador2):
        self.juego = juego
        self.jugador = [None, jugador1, jugador2]
    
    def muestra_estado(self, s):
        """
        Muestra el estado del juego
        
        """
        raise NotImplementedError("Hay que desarrollar este método, pues")
    
    def muestra_ganador(self, ganancia):
        """
        Muestra el ganador del juego, al finalizar
        
        """
        raise NotImplementedError("Hay que desarrollar este método, pues")

    def jugador_humano(self, s, j):
        """
        Pide al usuario que ingrese una jugada, y la devuelve
        
        """
        raise NotImplementedError("Hay que desarrollar este método, pues")

    def pide_jugada(self, jugador, s, j):
        """
        Pide al jugador escoger la jugada a realizar, entre las acciones posibles

        Regresa la acción escogida por el usuario, por defalt, se asume que el jugador es una interface
        
        """
        if isinstance(self.jugador[j], Jugador):
            return self.jugador[j].jugada(self.juego, s, j)
        else:
            return self.jugador_humano(s, j)

    def juega(self, max_pasos=1_000):
        """
        Juega el juego, mostrando el estado del juego, y al finalizar, muestra el ganador
        
        """
        s = self.juego.inicializa()
        self.muestra_estado(s)
        j = 1
        pasos = 0
        while not self.juego.terminal(s) and pasos < max_pasos:
            a = self.pide_jugada(self.jugador[j], s, j)
            s = self.juego.sucesor(s, a, j)
            self.muestra_estado(s)
            j = -j
            pasos += 1
        self.muestra_ganador(self.juego.ganancia(s))
        

class Jugador:
    """
    Clase abstracta para un jugador, que recibe el estado del juego y devuelve la jugada a realizar
    """
    def jugada(self, juego, s, j):
        """
        Devuelve la jugada a realizar por el jugador j en el estado s del juego
        
        """
        raise NotImplementedError("Hay que desarrollar este método, pues")


class JugadorAleatorio(Jugador):
    """
    Jugador que escoge una jugada al azar entre las legales
    """
    def jugada(self, juego, s, j):
        return choice(list(juego.jugadas_legales(s, j)))


def minimax(juego, s, j):
    """
    Devuelve la mejor jugada para el jugador en el estado
    
    """
    def max_val(s, j):
        if juego.terminal(s):
            return j * juego.ganancia(s)
        v = -1e10
        for a in juego.jugadas_legales(s, j):
            v = max( v, min_val( juego.sucesor(s, a, j), -j))
        return v
    
    def min_val(s, j):
        if juego.terminal(s):
            return -j * juego.ganancia(s)
        v = 1e10
        for a in juego.jugadas_legales(s, j):
            v = min( v, max_val(juego.sucesor(s, a, j), -j))   
        return v
    
    return max(
        juego.jugadas_legales(s, j),
        key=lambda a: min_val( juego.sucesor(s, a, j), -j))
    
class JugadorMinimax(Jugador):
    """
    Jugador que escoge la mejor jugada usando minimax
    """
    def jugada(self, juego, s, j):
        return minimax(juego, s, j)


def alpha_beta(juego, s, j, ordena=None):
    """
    Devuelve la mejor jugada para el jugador en el estado
    
    """
    if ordena is not None and not callable(ordena):
        raise ValueError("El argumento ordena debe ser una función o None")
    elif ordena is None:
        def _ordena(lista):
            shuffle(lista)
            return lista
        ordena = _ordena

    def max_val(s, j, alfa, beta):
        if juego.terminal(s):
            return j * juego.ganancia(s)
        v = -1e10
        jugadas = ordena(list(juego.jugadas_legales(s, j)))
        for a in jugadas:
            v = max(v, min_val(juego.sucesor(s, a, j), -j, alfa, beta))
            if v >= beta:
                return v
            alfa = max(alfa, v)
        return alfa
    
    def min_val(s, j, alfa, beta):
        if juego.terminal(s):
            return -j * juego.ganancia(s)
        v = 1e10
        jugadas = ordena(list(juego.jugadas_legales(s, j)))
        for a in jugadas:
            v = min( v, max_val(juego.sucesor(s, a, j), -j, alfa, beta))
            if v <= alfa:
                return v
            beta = min(beta, v)
        return beta
    
    jugadas = ordena(list(juego.jugadas_legales(s, j)))
    return max(
        jugadas,
        key=lambda a: min_val(juego.sucesor(s, a, j), -j, -1e10, 1e10))

class JugadorAlphaBeta(Jugador):
    """
    Jugador que escoge la mejor jugada usando alpha-beta
    """
    def __init__(self, ordena=None):
        self.ordena = ordena
    
    def jugada(self, juego, s, j):
        return alpha_beta(juego, s, j, self.ordena)