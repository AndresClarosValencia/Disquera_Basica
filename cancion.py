class Cancion():
    def __init__(self,nombre,autor,genero,año_lanzamiento):
        self.nombre=nombre;
        self.autor=autor;
        self.genero=genero;
        self.año_lanzamiento=año_lanzamiento;
    def __str__(self):
        return ("La canción: {} \n Del autor: {} \n Del género: {} \n Del año: \n Se creo correctamente".format(self.nombre,self.autor,self.genero,self.año_lanzamiento));
