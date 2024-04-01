#
# Biblioteca # Foro ADICRA 2024-03-23
#
#import microbit
import biblioteca
from time import sleep
microbit_sleep = sleep
microbit_display_scroll=print
contador = 0
while True:
    microbit_display_scroll(contador)
    contador = contador+1
    microbit_sleep(1)
    biblioteca.miFuncion()



