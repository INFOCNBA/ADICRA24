x = "global"
def f():
    x = "enclosing"
    def g():
        print(x) #sacamos la primitiva `nonlocal` y la asignación
    g()
    print(x)
f()
print(x)