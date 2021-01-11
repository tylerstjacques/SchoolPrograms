s = input('enter a string')


def punct(s):
    p = s.count('.')
    e = s.count('!')
    q = s.count('?')
    t = int(q)+int(e)+int(p)
    print(t)


punct(s)
