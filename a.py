""" 
    t: lista liczności drużyn
    a: pojemność klubu
    i: indeks aktualnie rozpatrywanej drużyny
    c: lista aktualnie rozpatrywanych drużyn
    r: lista wszystkich znalezionych kombinacji
"""
def f(t, a, i, c, r):
    if a == 0:
        r.append(c[:])
        return
    if a < 0 or i >= len(t):
        return
    f(t, a - t[i], i + 1, c + [t[i]], r)
    f(t, a, i + 1, c, r)


# przykladowe wywolanie
t = [20, 15, 10, 5, 5]
a = 25
r = []
f(t, a, 0, [], r)
print(r)