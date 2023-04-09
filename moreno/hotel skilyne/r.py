import sqlite3
conex=sqlite3.connect('D:\hotel skilyne/22basesdedatos.db')
cur=conex.cursor()

#print(conex)

def seleccion():
   sentencia=f"SELECT * FROM Habitaciones"# WHERE {n_habitacion} {tipo_habitacion} {precio}
   print(sentencia)
   list=cur.execute(sentencia)
   return list.fetchall()

print((4, 'Fedora', 'Jauncey'))


def update():
   n=int(input("Ingrese el numero de habitacion que desea actualizar"))
   t=input("Ingrese el tipo de habitacion que desea actualizar")
   p=int(input("Ingrese el precio que desea actualizar"))
   s=f'UPDATE Habitaciones SET{n_habitacion}='{precio}' 'WHERE tipo_habitacion'
   print(s)
   cur.execute(s)
   print("Se actualizaron correctamente los datos")


m('Fedora','nombre','Mick')


def insert():
   n=int(input("Ingrese e numero de la habitacion"))
   t=input("Ingrese el tipo de habitacion")
   p=int(input("Ingrese el precio"))
   s=f"INSERT INTO Habitaciones VALUES ('{n}','{t}'.{p}')"
   cur.execute(s)
   print("Todos los datos fueron creados correctamente")


def delete ():
   n=int(input('Que numero de habitacion quiere eliminar'))
   s=f"DELETE FROM Habitaciones WHERE tipo_habitacion"
   cur.execute(s)
   print("Se a elinado correctamente todos los datos")



insert()
delete() 
update()
     