# WAF to print each element of list

L = (56, 45, 65, 98, 75, 32)

def el(items, idx=0):
    if len(items) == idx:
        return 'no element'
    print(items[idx])
    el(items, idx + 1)

el(L)
