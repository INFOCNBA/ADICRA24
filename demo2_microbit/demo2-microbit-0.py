x = "global"
def f():
    def g():
        print(x)
    g()
    print(x)
f()
print(x)