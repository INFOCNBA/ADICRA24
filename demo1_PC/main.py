serial_write_string=print
serial_write_number=print

def funcion(param):
    param.append(4) #largo 4
    lista.append(5)#largo  ??
    
lista = [1, 2, 3]
serial_write_string("\nlargo de la lista\n")
serial_write_number(len(lista))
funcion(lista)
serial_write_string("\nlargo de la lista\n")
serial_write_number(len(lista))
