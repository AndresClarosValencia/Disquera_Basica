import os;
from mlibreria import Metodos_libreria;


class Menu():
    def __init__(self):
        self.metodos=Metodos_libreria();
    def limpiar_pantalla(self):
        os.system('cls');
    
    def opciones(self):

        self.limpiar_pantalla();
        print("Bienvenido usuario , selecciona una opción");
        print("1)Agregar una canción");
        print("2)Mostrar canciones");
        print("3)Buscar canciones)");
        print("4)Elimincar canciones");
        print("5)Descargar canciones");
        print("6)Salir");
        while(True):
            try:
                opcion1=int(input("\n Opción: "));
            except ValueError:
                print("Ingresa una opción valida");
            else:
                if(opcion1==1):
                    self.metodos.agregar();
                    self.devolver();
                elif(opcion1==2):
                    self.metodos.mostrar();
                    self.devolver();
                elif(opcion1==3):
                    self.metodos.buscar();
                    self.devolver();
                elif(opcion1==4):
                    self.metodos.eliminar();
                    self.devolver();
                elif(opcion1==5):
                    self.metodos.descargar();
                    self.devolver();
                else:
                    print("Gracias por tu tiempo");
                break
    
    def devolver(self):
        while(True):
            try:
                print("\nDesea devolverse al menú principal:\n");
                opcion2=input("1)Si   2)No \n");
                
            except ValueError:
                print("Selecciona una opción valida");
            
            else:
                if opcion2.lower()=='si':
                    a=0;
                    while(a==0):
                        return self.opciones();
                elif opcion2=='no':
                    print("Gracias por tú tiempo");        
                    break
                