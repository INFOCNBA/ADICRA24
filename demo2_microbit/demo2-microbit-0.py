#
# https://realpython.com/python-namespaces-scope/
#
# Basado en `Example 1: Single Definition`
#

x = "global"
def f():
    def g():
        print(x)
    g()
    print(x)
f()
print(x)