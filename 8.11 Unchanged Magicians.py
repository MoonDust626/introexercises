magician_names = ['james', 'randy', 'john', 'will', 'carol', 'tanya']
magician_great = []

def make_great(magicians):
    for magician in magicians:
        magician_great.append(magician.title() + ' The Great')

make_great(magician_names)
print(magician_names)
print(magician_great)