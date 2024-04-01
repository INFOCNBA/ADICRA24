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