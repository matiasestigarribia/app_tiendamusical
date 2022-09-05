from tkinter import *
from tkinter import ttk

mi_id = 0

maintienda = Tk()
maintienda.config(bg="#6666E6")
maintienda.resizable(width=300, height=200)

var_artista = StringVar()
var_album = StringVar()
var_unidades = StringVar()
var_valor = StringVar()

#########################
# labels

# mi_id = Label(maintienda, text="ID") #para agregar entry para ID o futuro display
# mi_id.grid(row=0, column=0, sticky=W)
artista = Label(maintienda, text="Artista")
artista.grid(row=1, column=0, sticky=W)
album = Label(maintienda, text="Album")
album.grid(row=2, column=0, sticky=W)
unidades = Label(maintienda, text="Unidades")
unidades.grid(row=3, column=0, sticky=W)
valor = Label(maintienda, text="Valor")
valor.grid(row=4, column=0, sticky=W)

#########################
# campos de entrada
entry_artista = Entry(maintienda, textvariable=var_artista, width=35)
entry_artista.grid(row=1, column=1)
entry_album = Entry(maintienda, textvariable=var_album, width=35)
entry_album.grid(row=2, column=1)
entry_unidades = Entry(maintienda, textvariable=var_unidades, width=35)
entry_unidades.grid(row=3, column=1)
entry_valor = Entry(maintienda, textvariable=var_valor, width=35)
entry_valor.grid(row=4, column=1)


#########################
# funciones botones


def funcion_alta():
    global mi_id
    mi_id += 1
    tree.insert(
        "",
        "end",
        text=str(mi_id),
        values=(
            var_artista.get(),
            var_album.get(),
            var_unidades.get(),
            var_valor.get(),
        ),
    )


def funcion_baja():
    global mi_id
    item = tree.focus()  # busca un valor determinado
    print(item)
    tree.delete(item)
    mi_id -= 1


def funcion_modificar():
    global mi_id
    item = tree.focus()  # busca un valor determinado, falta desarrollo de modificar
    print(item)
    tree.delete(item)
    mi_id -= 1


def funcion_listar():
    global mi_id
    item = tree.focus()
    print(item)


tree = ttk.Treeview(maintienda)
tree["columns"] = ("col1", "col2", "col3", "col4")
tree.column("#0", minwidth=50, anchor=W)
tree.column("col1", minwidth=60, anchor=W)
tree.column("col2", minwidth=60, anchor=W)
tree.column("col3", minwidth=20, anchor=W)
tree.column("col4", minwidth=30, anchor=W)

tree.grid(column=0, row=7, columnspan=4)

########################
# botones
boton_g = Button(maintienda, text="Agregar", command=funcion_alta)
boton_g.grid(row=6, column=0)
boton_e = Button(maintienda, text="Eliminar", command=funcion_baja)
boton_e.grid(row=6, column=1)
boton_m = Button(maintienda, text="Modificacion", command=funcion_modificar)
boton_m.grid(row=6, column=2)
boton_v = Button(maintienda, text="Ver", command=funcion_listar)
boton_v.grid(row=6, column=3)


maintienda.mainloop()
