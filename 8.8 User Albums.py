def make_album(name, title, track_number = ''):
    if track_number:
        album_title = {'Artist': name, 'Record': title, 'number of tracks':track_number}
    else:
        album_title = {'Artist': name, 'Record': title}
    return album_title

while True:
    print('\nEnter the Album Name followed by the Title')
    print("(enter 'q' at any time to quit)")

    l_album = input("Album name: ")
    if l_album == 'q':
        break
    l_title = input("Title name: ")
    if l_title == 'q':
        break

    formatted_album = make_album(l_album, l_title)
    print(formatted_album)

