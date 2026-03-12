import juegos_simplificado as js

class tiktaktoe(js.JuegoZT2):
    """El juego ultimate tik tak toe"""
    def init():
        t = tuple(80 * [0])
        t = t[:80] + (-2, -2)
        return t
    
    def jugadas_legales(self, s, j):
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
            
    def sucesor(self, s, a, j):
        if s[a] != 0:
            raise ValueError("Celda ocupada")
        
        tablero = s[:81]
        nuevo_tablero = tablero[:a] + (j,) + tablero[a+1:]

        if j == 1:
            jugada1 = a
            jugada2 = s[82]
        else:
            jugada1 = s[81]
            jugada2 = a

        return nuevo_tablero + (jugada1, jugada2)