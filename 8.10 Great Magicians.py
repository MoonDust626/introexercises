magician_names = ['james', 'randy', 'john', 'will', 'carol', 'tanya']

def magician_namer(namer):
    for name in namer:
        msg = 'Welcome the awe inspiring, ' + name.title() + '!'
        print(msg)

def make_great(magicians):
    for magician in magicians:
        great = magician + 'The Great'
        return great

make_great(magician_names)
magician_namer(magician_names)