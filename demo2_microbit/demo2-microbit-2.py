#
# https://realpython.com/python-namespaces-scope/
#
# Basado en `Example 3: Triple Definition`  y también en
# Basado en `Example 4: No Definition`
#

x = "global"
def f():
    x = "enclosing"
    def g():
        print(x) # ésta línea no está en el original `Example 3: Triple Definition`
        x = "local"
        print(x)
    g()
    print(x)
f()
print(x)