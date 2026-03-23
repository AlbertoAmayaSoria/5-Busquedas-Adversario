import juegos_simplificado as js

class tiktaktoe(js.JuegoZT2):
    """Juego ultimate tik tak toe"""
    def init(self):
        return tuple([0] * 81 + [-2])
    
    BLOQUES = {
        (i, j): [(i*3 + r)*9 + (j*3 + c)
                 for r in range(3)
                 for c in range(3)]
        for i in range(3)
        for j in range(3)
    }

    def jugadas_legales(self, s, j):
        ultima = s[81]

        #Primera jugada
        if ultima == -2:
            return [i for i in range(81) if s[i] == 0]
        
        fila = ultima // 9
        col = ultima % 9

        bf = fila % 3
        bc = col % 3

        bloque = self.BLOQUES[(bf, bc)]
        libres = [i for i in bloque if s[i] == 0]

        # si el bloque tiene espacio
        if libres:
            return libres
        
        # si el bloque est lleno
        return [i for i in range(81) if s[i] == 0]
        
    def gano_bloque(self, tablero, bf, bc, j):

        bloque = self.BLOQUES[(bf,bc)]

        c = [tablero[i] for i in bloque]

        lineas = [
            # Izquierda-Derecha
            (0,1,2),(3,4,5),(6,7,8),
            # Arriba-Abajo
            (0,3,6),(1,4,7),(2,5,8),
            # Diagonales
            (0,4,8),(2,4,6)
        ]

        for a,b,c_ in lineas:
            if c[a] == c[b] == c[c_] == j:
                return True

        return False

    def sucesor(self, s, a, j):
        if s[a] != 0:
            raise ValueError("Celda ocupada")
        
        tablero = list(s[:81])
        tablero[a] = j

        fila = a // 9
        col = a % 9

        bf = fila // 3
        bc = col // 3

        if self.gano_bloque(tablero, bf, bc, j):
            # Marcar como bloque ganado

        tablero = tuple(tablero)

        if j == 1:
            jugada1 = a
            jugada2 = s[82]
        else:
            jugada1 = s[81]
            jugada2 = a

        return tablero + (jugada1, jugada2)


    def terminal(self, s):
        #Revisar dónde se debe actualizar un "gato" pequeño para cambiarlo por completo a un valor
        #Revisar si hay 3 bloques con el mismo número consecutivos
        