#
# Biblioteca # Foro ADICRA 2024-03-23
#
import microbit
import biblioteca
contador = 0
while True:
    microbit.display.scroll(contador)
    print(contador)
    contador = contador+1
    microbit.sleep(1000)
    biblioteca.miFuncion()



