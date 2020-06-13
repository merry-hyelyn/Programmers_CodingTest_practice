def solution(genres, plays):
    answer = []
    albums = {}

    for i in range(len(genres)):
        if genres[i] in albums:
            albums[genres[i]] += plays[i]
        else:
            albums[genres[i]] = plays[i]
    
    length = len(albums)
    play_list = []

    for i in range(length):
        album = max(albums.keys())

        for i, genre in enumerate(genres):
            if genre == album:
                if plays[i] not in play_list:
                    play_list.append(plays[i])
        
        l = len(play_list)
        cnt =0

        for i in range(l):
            cnt += 1
            if cnt >= 3:
                break
            play = max(play_list)
            answer.append(plays.index(play))
            play_list.remove(play)

        play_list = []
        albums.pop(album)

    return answer

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],[800, 600, 150, 800, 2500]))