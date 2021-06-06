magician_names = ['james', 'randy', 'john', 'will', 'carol', 'tanya']

def magician_namer(namer):
    for name in namer:
        msg = 'Welcome the awe inspiring, ' + name.title() + '!'
        print(msg)

magician_namer(magician_names)