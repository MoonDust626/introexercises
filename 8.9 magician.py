magician_names = ['james', 'randy', 'john', 'will', 'carol', 'tanya']

def show_magicians(namer):
    for name in namer:
        msg = 'Welcome the awe inspiring, ' + name.title() + '!'
        print(msg)

show_magicians(magician_names)