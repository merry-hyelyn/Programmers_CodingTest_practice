def solution(genres, plays):
    answer = []
    albums = {}

    for i in range(len(genres)):
        if genres[i] in albums:
            albums[genres[i]] += plays[i]
        else:
            albums[genres[i]] = plays[i]
    album_list = sorted(albums.items(), key=(lambda x: x[1]), reverse=True)
    play_list = {}

    for k in album_list:
        for i,value in enumerate(genres):
            if k[0] == value:
                play_list[i] = plays[i]
        
        result = sorted(play_list.items(), key=(lambda x: x[1]), reverse=True)
        for i in range(2):
            answer.append(result[i][0])

        play_list = {}
    return answer

print(solution(['classic','pop','classic','pop','classic','classic'],[400,600,150,2500,500,500] ))