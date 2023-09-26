#Importación de la clase Cancion
from cancion import Cancion;
import os;


class Metodos_libreria():
    def __init__(self):
        self.lista_canciones=[];
        self.lista_canciones_descargadas=[];
        self.cancion_agregada=None;
        
    def limpia_pantalla(self):
        os.system('cls');
    
    def agregar(self):
        #Aplicando excepciones
        while(True):
            try:
                #Creando objeto canción
                cancion_agregada=Cancion("","","",0);
                print("Desea agregar una canción a la disquera \n 1)Si  2)No \n");
                op1=input();
                if op1.lower()=='si':
                    print("Digite los datos de la canción:\n");
                    cancion_agregada.nombre=input("\nNombre de la canción: ");
                    cancion_agregada.autor=input("\nAutor de la canción: ");
                    cancion_agregada.genero=input("\nGénero de la canción: ");
                    cancion_agregada.año_lanzamiento=int(input("\nAño de la canción:"));
                    self.lista_canciones.append(cancion_agregada);
                    self.cancion_agregada=cancion_agregada;
            except ValueError:
                self.limpia_pantalla();
                print("Ingresa el año correctamente");
            else:
                print("\nGracias por su tiempo, canción agregada correctamente");
                print("\n¿Desea agregar una  canción extra? \n");
                op3=input("1)SI  2)No \n");
                if op3.lower()=='si':
                    self.limpia_pantalla();
                    return self.agregar();
                else:
                    print("\nTen un buen día!");
                break
    
    def mostrar(self):
        self.limpia_pantalla();
        print("Canciones  actuales en la disquera: ",len(self.lista_canciones));
        i=0;
        for a in self.lista_canciones:
            i+=1;
            print(i,")",a.nombre,"\n");
    
    def mostrar_descargas(self):
        self.limpia_pantalla();
        print("Canciones  actuales descargadas: ",len(self.lista_canciones_descargadas));
        i=0;
        for a in self.lista_canciones_descargadas:
            i+=1;
            print(i,")",a.nombre,"\n");

    def buscar(self):
        validador=False;
        print("Ingresa el titulo que deseas buscar:");
        nombre=input().lower();
        for a in self.lista_canciones:
            if nombre.lower()==a.nombre.lower():
                print("La canción: {} esta en la lista de canciones".format(a.nombre));
                validador=True;
                print("¿Desea realizar otra búsqueda? \n 1)Si  2)No \n");
                op4=input().lower();
                if op4=='si':
                    return self.buscar();
                else:
                    print("Gracias por tu tiempo");
                break
        if not validador:
            print("La canción {} no esta en la lista".format(nombre));
            print("¿Desea realizar otra búsqueda? \n 1)Si  2)No \n");
            op4=input().lower();
            if op4=='si':
                return self.buscar();
            else:
                print("Gracias por tu tiempo");
    
    def eliminar(self):
        validador2=False;       
        cancion_eliminar=input("Ingresa el nombre de la canción que deseas eliminar: \n");
        for a in self.lista_canciones:
            if cancion_eliminar.lower()==a.nombre.lower():
                self.lista_canciones.remove(a);
                print("Canción eliminada correctamente");
                validador2=True;
                print("\n¿Desea eliminar otra canción? \n 1)Si  2)No \n");
                op5=input().lower();
                if op5=='si':
                    return self.eliminar();
                else:
                    print("Gracias por tu tiempo");
                break

        if not validador2:
            print("La canción {} no se logró eliminar".format(cancion_eliminar));
            print("\n¿Desea intentar eliminar otra canción? \n 1)Si  2)No \n");
            op5=input().lower();
            if op5=='si':
                return self.eliminar();
            else:
                print("Gracias por tu tiempo");
                return self.mostrar();

    def descargar(self):
        validador3=False;
        print("Ingresa el nombre de la canción que desea descargar : \n");
        cancion_descarga=input().lower();
        for a in self.lista_canciones:
            if cancion_descarga.lower()==a.nombre:
                self.lista_canciones_descargadas.append(a);
                validador3=True;
                print("La canción {} se descargo correctamente\n".format(cancion_descarga));
                print("Desea descargar otra canción");
                op6=input("1)Si  2)No \n");
                if op6.lower()=='si':
                    return self.descargar();
                else:
                    print("Gracias por tu tiempo");
                    return self.mostrar_descargas();
            
        if not validador3:
            print("No se logró descargar la canción {} ".format(cancion_descarga));
            print("Desea descargar otra canción");
            op6=input("1)Si  2)No \n");
            if op6.lower()=='si':
                return self.descargar();
            else:
                print("Gracias por tu tiempo");
                return self.mostrar_descargas();
                
        





