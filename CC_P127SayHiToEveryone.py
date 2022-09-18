def albums(singer, album, track = None):
    """定义记录专辑信息的函数"""
    albums = {'singer_name':singer, 'album_name':album}  #默认值为None的可选形参track 不需要写在这里
    if track:
        albums['track'] = track
    return albums

album1 = albums('王菲', '传奇', track = 2)
print(album1)
album2 = albums('周杰伦', '大艺术家')
print(album2)