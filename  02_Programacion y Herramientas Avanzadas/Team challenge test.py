pip install numpy
import random
import numpy as np
class Tablero:
    def __init__(self, name, tamano):
        self.tamano = tamano
        self.name = name
        self.tablero = self.CrearVacio(tamano)
        
    def CrearVacio(self, tamano):
        tablero = np.full((tamano,tamano)," ")
        print(tablero)
        return tablero
    
    def ubicador_barcos(self, eslora,ubicacion, orientacion):
        

        for i in range(eslora):
          
            if ubicacion[0] <0 or ubicacion[0] > self.tamano or ubicacion[1] <0 or ubicacion[1] > self.tamano:
                print("No se puede poner un barco en esa posición")
                break
            if self.tablero[ubicacion[0],ubicacion[1]] == "O":
                print("Ya hay un barco en esa posición")
                break
        
            self.tablero[ubicacion[0],ubicacion[1]] = "O"
        
            if orientacion == "n":
                ubicacion[0] = ubicacion[0] - 1
            elif orientacion == "s":
                ubicacion[0] = ubicacion[0] + 1
            elif orientacion == "e":
                ubicacion[1] = ubicacion[1] + 1
            elif orientacion == "o":
                ubicacion[1] = ubicacion[1] - 1
            else:
                print("Orientación no válida, solo n,s,e,o")
                break
        print(self.tablero)
        return self.tablero
    
    def disparo(self, ubicacion):
        if ubicacion[0] <0 or ubicacion[0] > self.tamano or ubicacion[1] <0 or ubicacion[1] > self.tamano:
            print("No se puede disparar a esa posición")
            
        elif self.tablero[ubicacion[0],ubicacion[1]] == "O":
            print("Tocado")
            self.tablero[ubicacion[0],ubicacion[1]] = "X"
        elif self.tablero[ubicacion[0],ubicacion[1]] == " ":
            self.tablero[ubicacion[0],ubicacion[1]] = "-"
            print("Agua")
        else:
            print("Ya habías disparado ahí")
        print(self.tablero)
        return self.tablero
    
    def BarcoAleatorio(self, eslora):
        
        orientacion = random.choice(["n","s","e","o"])
        ubicacion = [random.randint(0,self.tamano),random.randint(0,self.tamano)]
        self.ubicador_barcos(eslora,ubicacion,orientacion)
        return self.tablero

                
                

                
                
