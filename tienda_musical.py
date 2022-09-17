from tkinter import *
from tkinter.messagebox import *
import sqlite3
from tkinter import ttk
import re

####################


def conexion():
    con = sqlite3.connect("mibase.db")
    return con


def crear_tabla():
    con = conexion()
    cursor = con.cursor()
    sql = """CREATE TABLE discografica
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             artista varchar(50) NOT NULL,
             album varchar(50) NOT NULL,
             unidades real,
             valor real)
    """
    cursor.execute(sql)
    con.commit()


try:
    conexion()
    crear_tabla()
except:
    print("Hay un error")


def alta(artista, album, unidades, valor, tree):
    cadena = artista
    patron = "^[A-Za-záéíóú]*$"
    if re.match(patron, cadena):
        print(artista, album, unidades, valor)
        con = conexion()
        cursor = con.cursor()
        data = (artista, album, unidades, valor)
        sql = "INSERT INTO discografica(artista, album, unidades, valor) VALUES(?, ?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
        seleccion(tree)
    else:
        print("Error")


def consulta():
    global mi_id
    item = tree.focus()
    print(item)


def baja(tree):
    valores = tree.selection()
    print(valores)
    item = tree.item(valores)
    print(item)
    print(item["text"])
    mi_id = item["text"]

    con = conexion()
    cursor = con.cursor()
    data = (mi_id,)
    sql = "DELETE FROM discografica WHERE id = ?;"
    cursor.execute(sql, data)
    con.commit()
    tree.delete(valores)


def seleccion(mitreview):
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    sql = "SELECT * FROM discografica ORDER BY id ASC"
    con = conexion()
    cursor = con.cursor()
    datos = cursor.execute(sql)

    resultado = datos.fetchall()
    for fila in resultado:
        print(fila)
        mitreview.insert(
            "", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4])
        )


def modificar(artista, album, unidades, valor, tree):
    valores = tree.selection()
    print(valores)
    item = tree.item(valores)
    print(item)
    print(item["text"])
    mi_id = item["text"]
    data = (artista, album, unidades, valor, mi_id)
    sql = "UPDATE discografica SET artista = ?, album = ?, unidades = ?, valor = ? WHERE id = ?"
    con = conexion()
    cursor = con.cursor()
    cursor.execute(sql, data)
    con.commit()
    seleccion(tree)


####################

maintienda = Tk()
maintienda.config(bg="#494C59")
maintienda.title("Tienda de música")
maintienda.resizable(width=300, height=200)

var_artista, var_album, var_unidades, var_valor = (
    StringVar(),
    StringVar(),
    DoubleVar(),
    DoubleVar(),
)

artista = Label(
    maintienda,
    text="Artista",
    borderwidth=2,
    relief="groove",
    foreground="white",
    background="#6666E6",
    width=10,
)
artista.grid(row=1, column=0, sticky=W)
album = Label(
    maintienda,
    text="Album",
    borderwidth=2,
    relief="groove",
    foreground="white",
    background="#6666E6",
    width=10,
)
album.grid(row=2, column=0, sticky=W)
unidades = Label(
    maintienda,
    text="Unidades",
    borderwidth=2,
    relief="groove",
    foreground="white",
    background="#6666E6",
    width=10,
)
unidades.grid(row=3, column=0, sticky=W)
valor = Label(
    maintienda,
    text="Valor",
    borderwidth=2,
    relief="groove",
    foreground="white",
    background="#6666E6",
    width=10,
)
valor.grid(row=4, column=0, sticky=W)

####################

entry_artista = Entry(
    maintienda,
    textvariable=var_artista,
    width=35,
    background="#8B9DC3",
    foreground="white",
)
entry_artista.grid(row=1, column=1)
entry_album = Entry(
    maintienda,
    textvariable=var_album,
    width=35,
    background="#8B9DC3",
    foreground="white",
)
entry_album.grid(row=2, column=1)
entry_unidades = Entry(
    maintienda,
    textvariable=var_unidades,
    width=35,
    background="#8B9DC3",
    foreground="white",
)
entry_unidades.grid(row=3, column=1)
entry_valor = Entry(
    maintienda,
    textvariable=var_valor,
    width=35,
    background="#8B9DC3",
    foreground="white",
)
entry_valor.grid(row=4, column=1)

####################

tree = ttk.Treeview(maintienda)
tree["columns"] = ("col1", "col2", "col3", "col4")
tree.column("#0", minwidth=50, anchor=W)
tree.heading("#0", text="ID")
tree.column("col1", minwidth=60, anchor=W)
tree.heading("col1", text="Artista")
tree.column("col2", minwidth=60, anchor=W)
tree.heading("col2", text="Album")
tree.column("col3", minwidth=20, anchor=W)
tree.heading("col3", text="Unidades")
tree.column("col4", minwidth=30, anchor=W)
tree.heading("col4", text="Valor")

tree.grid(column=0, row=7, columnspan=4)

####################

boton_g = Button(
    maintienda,
    text="Agregar",
    command=lambda: alta(
        var_artista.get(), var_album.get(), var_unidades.get(), var_valor.get(), tree
    ),
    borderwidth=2,
    relief="groove",
    foreground="white",
    background="#6666E6",
)
boton_g.grid(row=6, column=0)
boton_e = Button(
    maintienda,
    text="Eliminar",
    command=lambda: baja(tree),
    borderwidth=2,
    relief="groove",
    foreground="white",
    background="#6666E6",
)
boton_e.grid(row=6, column=1)
boton_m = Button(
    maintienda,
    text="Modificacion",
    command=lambda: modificar(
        var_artista.get(), var_album.get(), var_unidades.get(), var_valor.get(), tree
    ),
    borderwidth=2,
    relief="groove",
    foreground="white",
    background="#6666E6",
)
boton_m.grid(row=6, column=2)
boton_v = Button(
    maintienda,
    text="Ver",
    command=lambda: consulta(),
    borderwidth=2,
    relief="groove",
    foreground="white",
    background="#6666E6",
)
boton_v.grid(row=6, column=3)

maintienda.mainloop()
