#import User_ini as User_ini
#import User as User
#import Flights as Flights

class Skyscanner():

    def __init__(self):
        pass
    def buscar_vuelo(self, ID):
        self.lista_Vuelos=[]
        f = open("src/API/Vuelos/Skyscanner.txt")
        linea = f.readline()
        while linea != "":
            id=linea
            if id==ID:
                linea = f.readline()
                nombre=linea
                linea = f.readline()
                precio=linea
                f.close()
                VueloDict = {
                    "ID": id,
                    "Nombre": nombre,
                    "precio": precio,
                }
                return VueloDict
            else:
                linea = f.readline()
                linea = f.readline()

            linea = f.readline()


        f.close()
        return  "No encontrado"

    def confirm_reserve(self, user, flights):
        return True
