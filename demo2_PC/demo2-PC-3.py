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
        nonlocal x
        print(x)
        x = "local"
        print(x)
    g()
    print(x)
f()
print(x)