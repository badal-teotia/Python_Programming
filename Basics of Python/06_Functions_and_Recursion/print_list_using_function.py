# WAF to print list arguments in one line

m = ("hero", "heroine", "make", "made", "built")

def list_series(name):
    for s in name:
        print(s, end=" ")

list_series(m)
print()
