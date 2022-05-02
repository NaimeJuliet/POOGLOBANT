class Persona:

    def _init_(self):
        self.__nombre=None
        self.__edad=None
        self.__telefono=None


    #siempre arranco por los
    #Getters (siempre son funciones e inician con la palabra def)
    #decorador de clase es una palabra que empieza por @, ante de la funcion y sigue con la palabra reservada property en el getter
    @property
    def nombre(self):
        return(self.__nombre)

    @property
    def edad(self):
        
        return(self.__edad)

    @property
    def telefono(self):
        return(self.__telefono)


    #Setters

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @edad.setter
    def edad(self,edad):
        if(edad<0):
            self.__edad=None
            print("edad erronea")
        else:
            self.__edad=edad
       
    
    @telefono.setter
    def telefono(self,telefono):
        self.__telefono=telefono  
    



    def saludar(self):
       print(f'Hola me llamo {self.__nombre}')
       print(f'mi edad es {self.__edad} y tengo sueño')