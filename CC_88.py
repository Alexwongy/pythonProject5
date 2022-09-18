def make_album(artist, title, tracks=0):
    """创建一个包含专辑信息的字典。"""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


# 生成提示语。
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "  # 让用户知道如何退出。
print("Enter 'quit' at any time to stop.")
while True:
    title = input(title_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break
    album = make_album(artist, title)
    print(album)
print("\nThanks for responding!")