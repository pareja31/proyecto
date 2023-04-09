class habitaciones :
    def __init__(self,n,t,p):
        self.n_habitacion=n
        self.tipo_habitacion=t
        self.precio=p

def getn_habitacion(self):
    return self.n_habitacion

def setn_habitacion(self,n_habitacion):
    self.n_habitacion=n_habitacion



def gettipo_habitacion(self):
    return self.tipo_habitacion

def settipo_habitacion(self,tipo_habitacion):
    self.tipo_habitacion=tipo_habitacion


def getprecio(self):
    return self.precio

def setprecio(self,precio):
    self.precio=precio


ho=habitaciones() 

print(ho.getn_habitacion())  
print(ho.gettipo_habitacion())  
print(ho.getprecio())    
ho.setn_habitacion()
ho.settipo_habitacion()
ho.setprecio()