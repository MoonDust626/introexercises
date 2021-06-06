magician_names = ['james', 'randy', 'john', 'will', 'carol', 'tanya']
magician_great = []

def magician_namer(namer):
    for name in namer:
        msg = 'Welcome the awe inspiring, ' + name.title() + '!'
        print(msg)


def make_great(magicians):
    magicians_len = len(magicians)
    for i in range(magicians_len):
        magicians[i] = magicians[i] + ' The Great'

make_great(magician_names[:])

magician_namer(magician_names)