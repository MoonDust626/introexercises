def make_album(name, title, track_number = ''):
    if track_number:
        album_title = {'artist': name, 'record': title, 'number of tracks':track_number}
    else:
        album_title = {'artist': name, 'record': title}
    return album_title

CD = make_album('Green Day', 'American Idiot', '11')
print(CD)

CD = make_album('Porter Robinson', 'Nurture')
print(CD)

CD = make_album('All American Rejects', 'Move Along')
print(CD)