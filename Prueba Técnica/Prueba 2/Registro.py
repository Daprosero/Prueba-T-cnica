from sympy import true
import time
import json
class Menu():
    def __init__(self):
        #Se inicializa dos diccionarios con las opciones de menú disponible y una lista vacía.
        self.menu={'1':self.Adicionar,'2':self.Modificar,'3':self.Eliminar,
        '4':self.Listar,'5':self.Cargar,'6':self.Guardar,'7':'Salir'}
        self.X=[]
        self.menu_key={'1':'Nombres','2':'Apellidos','3':'Edad','4':'Email','5':'Todo','6':'Salir'}
    #Esta función se encarga de mostrar en pantalla cada uno de los menú
    def Mostrar_menu(self,b=0):
        if b==1:
            print('------------------------------')
            print('   Menú Secundario         \n')
            print('\n 1 Nombres \n 2 Apellidos \n 3 Edad \n 4 Email \n 5 Todo \n 6 Salir ')
            print('------------------------------\n')
        else:
            print('------------------------------')
            print('   Menú Principal         \n')
            print(' 1 Adicionar Datos \n 2 Modificar Datos \n 3 Eliminar Datos \n 4 Listar Datos \n 5 Cargar Datos \n 6 Guardar Datos \n 7 Salir')
            print('------------------------------\n')
    # Esta función corre de manera indefinida el menú principal o el secundario, 
    # a menos, que se seleccione la opción 7 o 6 respectivamente 
    def Run(self):
        while True:
            self.Mostrar_menu()
            eleccion=input('Eliga una opción: ')
            print('\n')
            if eleccion=='7':
                break
            accion=self.menu.get(eleccion)
            if accion:
                if int(eleccion)==5:
                    path=input('Ingrese una ubicación del archivo: ')
                    accion(path)
                elif int(eleccion)==6:
                    self.Vacio()
                    path=input('Ingrese una ubicación del archivo: ')
                    accion(path)
                else:
                    accion()
            else:
                print('\n------------------------------\n Opción inválida: \n------------------------------\n')
    # Añade  a la lista la información de cada uno de los usuarios
    def Adicionar(self,id=None):
        Nombres=input('Ingrese los Nombres: ')
        Apellidos=input('Ingrese los Apellidos: ')
        Edad=input('Ingrese una edad: ')
        Email=input('Ingrese un Email: ')
        print(id)
        # Este if separa la adición de la modificación 
        if id==None:
            if len(self.X)==0:
                self.X.append({'id':0,'Nombres':Nombres,'Apellidos':Apellidos,'Edad':Edad,'Email':Email})
            else:
                ban=int(self.X[-1]['id'])+1
                self.X.append({'id':ban,'Nombres':Nombres,'Apellidos':Apellidos,'Edad':Edad,'Email':Email})  
        else:
            self.X[id]={'id':self.X[id]['id'],'Nombres':Nombres,'Apellidos':Apellidos,'Edad':Edad,'Email':Email}
        self.Listar()
    # Esta función nos da la opción de elegir si modificar aspectos específicos del usuario 
    # o toda la información 
    def Modificar(self):
        self.Listar()
        id=self.Verificar()
        while True:
            self.Mostrar_menu(b=1)
            eleccion=input('Eliga un valor a remplazar: ')
            print('\n')
            if eleccion =='1':
                Val=input('Ingrese los nuevos Nombres: ')
                self.Remplazo(id,'Nombres',Val)
                self.Listar()
            elif eleccion =='2':
                Val=input('Ingrese los nuevos Apellidos: ')
                self.Remplazo(id,'Apellidos',Val)
                self.Listar()
            elif eleccion =='3':
                Val=input('Ingrese la nueva Edad: ')
                self.Remplazo(id,'Edad',Val)
                self.Listar()
            elif eleccion =='4':
                Val=input('Ingrese el nuevo Email: ')
                self.Remplazo(id,'Email',Val)
                self.Listar()
            elif eleccion =='5':
                self.Adicionar(id) 
            elif eleccion =='6':
                self.Run()                               
            else:
                print('\n------------------------------\n Opción inválida: \n------------------------------\n')
    #Elimina la información correspondiente al identificador seleccionado.
    def Eliminar(self):
        self.Listar()
        id=self.Verificar(c=1)
        self.X.pop(id)
        self.Listar()
    # Muestra los datos
    def Listar(self):
        self.Vacio()
        for i in self.X:
            print('id: ',i['id'],',','Nombres: ',i['Nombres'],',','Apellidos: ',i['Apellidos'],',',
            'Edad: ',i['Edad'],',','Email: ',i['Email'],'\n')
        time.sleep(2)
    # Carga un archivo .json en la ubicación seleccionada
    def Cargar(self,path):
        with open(path+'.json') as json_file:
            self.X = json.loads(json.load(json_file))
        self.Listar()
    # Guarda un archivo .json en la ubicación seleccionada 
    def Guardar(self,path):
        json_string = json.dumps(self.X)
        with open(path+'.json', 'w') as outfile:
            json.dump(json_string, outfile)
    #Verifica si el id seleccionado es válido o si se desea cancelar la operación
    # Adicionalmente, entrega la posición en la que se encuentra dicho id. 
    def Verificar(self,c=0):
        while True:
            self.Vacio()
            if c==0:
                id= input('Ingrese un id Válido para modificar. Presione x si desea salir: ' )
            else:
                id= input('Ingrese un id Válido para eliminar. Presione x si desea salir: ' )
            if id=='x' or id=='X':
                self.Run()
            else:
                aux=0
                for i in self.X:
                    if i['id']==int(id):
                        return aux
                    aux=aux+1
    #Remplaza inforamción específica de un usuario
    def Remplazo(self,id,key,val):
        self.X[id][key]=val
    # Verifica si hay información a eliminar,modificar, visualizar o guardar. De lo contrario 
    # no realiza la acción determinada.
    def Vacio(self):
        if len(self.X)==0:
            print('No hay Datos \n')
            time.sleep(2)
            self.Run()
#Inicia la clase Menu y su función Run.        
if __name__ == '__main__':
    Menu().Run()