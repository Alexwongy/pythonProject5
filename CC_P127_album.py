def make_album(singer_name, album_name, tracks = None):
    """描述音乐专辑的字典"""
    album = {'singer':singer_name, 'album':album_name, }
    if tracks:
        album['tracks'] = tracks
    return album


album1 = make_album('那英', '相约98',tracks = 4)
album2 = make_album('王菲', '传奇')
album3 = make_album('Jolin', '大艺术家')
print(album1 )
print(album2)
print(album3)

