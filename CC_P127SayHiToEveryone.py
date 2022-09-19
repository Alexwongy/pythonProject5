# def album_singer(albums, singers, tracks = None):
#     """定义一个记录唱片信息的函数"""
#     album = {'album_name':albums, 'singer_name':singers}
#     if tracks:
#         album['track'] = tracks
#     return album
#
#
# musician = album_singer('lover forever', 'Lili')
# print(musician)

# def album_singer(album_name, singer_name,track = None):
#     """这是记录专辑信息的函数"""
#     album = {'singer':singer_name, 'album':album_name}
#     if track:
#         album['track'] = track
#     return album
#
#
#
#
# while True:
#     print('\nplease enter the information of the album')
#     print("\nEnter 'q' at any time to quit")
#
#     SingerName = input('the name of the singer:')
#     if SingerName == 'q':
#         break
#
#
#     AlbumName = input('the name of the alnbum: ')
#     if AlbumName == 'q':
#         break
#
#     TrackNum = int(input('the number of the tracks') )
#     if TrackNum == 'q':
#         break
#
#     print(album_singer(AlbumName, SingerName))

#要怎么免于输入将track 变成一个可选形参，不输入也不会报错



#say hello to everyone
def greet_users(names):
    """向列表中每个用户发出问候"""
    for name in names:
        msg = f"Hello，{name.title()}"
        print(msg)


usernames = ['hannah', 'KC', 'helen']#要与初始位置对齐
greet_users(usernames)