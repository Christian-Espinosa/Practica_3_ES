# -*- coding: utf-8 -*-
"""
Created on Wed May 20 05:16:41 2020

@author: usuari

-Dado un viaje con múltiples destinos y más de un viajero,cuando se produce un
error al confirmar los vehículos, se reintenta realizar la confirmación
-Dado un viaje con múltiples destinos y más de un viajero, cuando la confirmación de los vehículos se realiza correctamente en un reintento, se
reporta que la acción se ha realizado correctamente
-Dado un viaje con múltiples destinos y más de un viajero,cuando se produceun
error al confirmar los vehículos, y se ha superado el número máximo de
reintentos, se reporta que la acción no se ha podido realizar
"""
import os
import sys
import unittest
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
PROJECT_DIR = os.path.join(PROJECT_DIR, '..', 'src')
if not PROJECT_DIR is sys.path:
    sys.path.insert(0, PROJECT_DIR)


from unittest import mock

from API.Coche import Rentalcars as Rentalcars
from API.Coche import Cars as Cars
from API.Airhopping import User as User

from Viaje import Viaje as Viaje
from Viatgers import Viatgers
from Destinos import Destinos

from API.Airhopping import User as User
from API.Vuelos import Skyscanner as Skyscanner
from API.Vuelos import Flights as Flights
from API.Airhopping import Booking as Booking
from API.Airhopping import Hotels as Hotels

from CalcularPrecio import CalcularPrecio

from API.Coche import Rentalcars as Rentalcars
from API.Coche import Cars as Cars

class Test_mock_reserva_vehiculoV5(unittest.TestCase):






    @mock.patch('API.Coche.Cars')
    def test_reintent_confirmacio(self, mock_reserva_vehiculo):
        sumPrecio=0

        Destinos_t2 = Destinos()
        Viajeros_t2 = Viatgers()

        User_t2 = User.User()
        Usuario_t2 = User_t2.getDatosUser("787372-P")


        Viajeros_t2.add_viatger("Alex","Alaminos","12345678P","23")
        Viajeros_t2.add_viatger("Anna","Dot","98765432P","20")

        sc_dic2=Skyscanner.Skyscanner().buscar_vuelo("f001")
        if sc_dic2!="No encontrado":
            v_obj_t2=Flights.Flights(sc_dic2['ID'],sc_dic2['precio'])#id, precio

            bk_dic2=Booking.Booking().buscar_hotel("h001")
            if bk_dic2!="No encontrado":
                h_obj_t2=Hotels.Hotels(2, bk_dic2['ID'], 1, 1, bk_dic2['Nombre'])
                h_obj_t2.setPrecio(bk_dic2['precio'])#precio


                #Hotel + Vuelo
                sumPrecio+=(float(bk_dic2['precio'])*int(h_obj_t2.dias)*int(h_obj_t2.numHab))
                sumPrecio+=(float(sc_dic2['precio'])*int(Viajeros_t2.get_num_viatgers()))

                Destinos_t2.add_destino("d001",v_obj_t2,h_obj_t2)
                rc_dic3=Rentalcars.Rentalcars().buscar_coche("C_302165")
                if rc_dic3!="No encontrado":
                    c_obj_t3=Cars.Cars(rc_dic3['Matricula'], rc_dic3['precio'], 1)
                    Destinos_t2.get_destino("d001").set_vehiculo(c_obj_t3)

                    sumPrecio+=(float(rc_dic3['precio'])*int(c_obj_t3.get_dias()))


        sc_dic2=Skyscanner.Skyscanner().buscar_vuelo("f002")
        if sc_dic2!="No encontrado":
            v_obj_t2=Flights.Flights(sc_dic2['ID'],sc_dic2['precio'])#id, precio

            bk_dic2=Booking.Booking().buscar_hotel("h002")
            if bk_dic2!="No encontrado":
                h_obj_t2=Hotels.Hotels(1, bk_dic2['ID'], 1, 1, bk_dic2['Nombre'])
                h_obj_t2.setPrecio(bk_dic2['precio'])#precio


                #Hotel + Vuelo
                sumPrecio+=(float(bk_dic2['precio'])*int(h_obj_t2.dias)*int(h_obj_t2.numHab))
                sumPrecio+=(float(sc_dic2['precio'])*int(Viajeros_t2.get_num_viatgers()))

                Destinos_t2.add_destino("d002",v_obj_t2,h_obj_t2)

                rc_dic3=Rentalcars.Rentalcars().buscar_coche("1234ABC")
                if rc_dic3!="No encontrado":
                    c_obj_t3=Cars.Cars(rc_dic3['Matricula'], rc_dic3['precio'], 1)
                    Destinos_t2.get_destino("d002").set_vehiculo(c_obj_t3)

                    sumPrecio+=(float(rc_dic3['precio'])*int(c_obj_t3.get_dias()))

                    Viaje_t2 = Viaje("v001", Viajeros_t2, Destinos_t2, Usuario_t2)

        self.assertTrue(mock_reserva_vehiculo.confirmar(Viaje_t2.get_user(),Viaje_t2.get_vehiculos()))
        mock_reserva_vehiculo.confirmar.return_value = False
        self.assertFalse(mock_reserva_vehiculo.confirmar(Viaje_t2.get_user(),Viaje_t2.get_vehiculos()))
        
        
        mock_reserva_vehiculo.confirmar.return_value = False
        if(not mock_reserva_vehiculo.confirmar(Viaje_t2.get_user(),Viaje_t2.get_vehiculos())):
            mock_reserva_vehiculo.confirmar.return_value = True
        self.assertTrue(mock_reserva_vehiculo.confirmar(Viaje_t2.get_user(),Viaje_t2.get_vehiculos()))



        def test_maxim_reintent(self, mock_reserva_vehiculo):
            sumPrecio=0

            Destinos_t2 = Destinos()
            Viajeros_t2 = Viatgers()

            User_t2 = User.User()
            Usuario_t2 = User_t2.getDatosUser("787372-P")


            Viajeros_t2.add_viatger("Alex","Alaminos","12345678P","23")
            Viajeros_t2.add_viatger("Anna","Dot","98765432P","20")

            sc_dic2=Skyscanner.Skyscanner().buscar_vuelo("f001")
            if sc_dic2!="No encontrado":
                v_obj_t2=Flights.Flights(sc_dic2['ID'],sc_dic2['precio'])#id, precio

                bk_dic2=Booking.Booking().buscar_hotel("h001")
                if bk_dic2!="No encontrado":
                    h_obj_t2=Hotels.Hotels(2, bk_dic2['ID'], 1, 1, bk_dic2['Nombre'])
                    h_obj_t2.setPrecio(bk_dic2['precio'])#precio


                    #Hotel + Vuelo
                    sumPrecio+=(float(bk_dic2['precio'])*int(h_obj_t2.dias)*int(h_obj_t2.numHab))
                    sumPrecio+=(float(sc_dic2['precio'])*int(Viajeros_t2.get_num_viatgers()))

                    Destinos_t2.add_destino("d001",v_obj_t2,h_obj_t2)
                    rc_dic3=Rentalcars.Rentalcars().buscar_coche("C_302165")
                    if rc_dic3!="No encontrado":
                        c_obj_t3=Cars.Cars(rc_dic3['Matricula'], rc_dic3['precio'], 1)
                        Destinos_t2.get_destino("d001").set_vehiculo(c_obj_t3)

                        sumPrecio+=(float(rc_dic3['precio'])*int(c_obj_t3.get_dias()))


            sc_dic2=Skyscanner.Skyscanner().buscar_vuelo("f002")
            if sc_dic2!="No encontrado":
                v_obj_t2=Flights.Flights(sc_dic2['ID'],sc_dic2['precio'])#id, precio

                bk_dic2=Booking.Booking().buscar_hotel("h002")
                if bk_dic2!="No encontrado":
                    h_obj_t2=Hotels.Hotels(1, bk_dic2['ID'], 1, 1, bk_dic2['Nombre'])
                    h_obj_t2.setPrecio(bk_dic2['precio'])#precio


                    #Hotel + Vuelo
                    sumPrecio+=(float(bk_dic2['precio'])*int(h_obj_t2.dias)*int(h_obj_t2.numHab))
                    sumPrecio+=(float(sc_dic2['precio'])*int(Viajeros_t2.get_num_viatgers()))

                    Destinos_t2.add_destino("d002",v_obj_t2,h_obj_t2)

                    rc_dic3=Rentalcars.Rentalcars().buscar_coche("1234ABC")
                    if rc_dic3!="No encontrado":
                        c_obj_t3=Cars.Cars(rc_dic3['Matricula'], rc_dic3['precio'], 1)
                        Destinos_t2.get_destino("d002").set_vehiculo(c_obj_t3)

                        sumPrecio+=(float(rc_dic3['precio'])*int(c_obj_t3.get_dias()))

                        Viaje_t2 = Viaje("v001", Viajeros_t2, Destinos_t2, Usuario_t2)

            self.assertTrue(mock_reserva_vehiculo.confirmar(Viaje_t2.get_user(),Viaje_t2.get_vehiculos()))
            mock_reserva_vehiculo.confirmar.return_value = False
            self.assertFalse(mock_reserva_vehiculo.confirmar(Viaje_t2.get_user(),Viaje_t2.get_vehiculos()))


        mock_reserva_vehiculo.confirmar.return_value = False
        if(not mock_reserva_vehiculo.confirmar(Viaje_t2.get_user(),Viaje_t2.get_vehiculos())):
            confirmacio=mock_reserva_vehiculo.confirmar(Viaje_t2.get_user(),Viaje_t2.get_vehiculos())
        if(not confirmacio):
            confirmacio=mock_reserva_vehiculo.confirmar(Viaje_t2.get_user(),Viaje_t2.get_vehiculos())
        if(not confirmacio):
            confirmacio=mock_reserva_vehiculo.confirmar(Viaje_t2.get_user(),Viaje_t2.get_vehiculos())
        
        
        #Comprovem que efectivament no es pot realitzar un altre confirmar reserva, el num conexions=0 significa que 
        # no es contactara amb l'API perque s'ha produit un exces d'intents
        if(mock_reserva_vehiculo.num_conexions==0):
            self.assertFalse(mock_reserva_vehiculo.confirmar(Viaje_t2.get_user(),Viaje_t2.get_vehiculos()))