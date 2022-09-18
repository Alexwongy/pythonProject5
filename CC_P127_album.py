def make_album(singer_name, album_name):
    """描述音乐专辑的字典"""
    album = {'singer':singer_name, 'album':album_name}
    return album


album1 = make_album('那英', '相约98')
album2 = make_album('王菲', '传奇')
album3 = make_album('Jolin', '大艺术家')
print(album1 )
print(album2)
print(album3)