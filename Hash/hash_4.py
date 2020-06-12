def solution(genres, plays):
    answer = []
    album = {}

    for i in range(len(genres)):
        if genres[i] in album:
            album[genres[i]] += plays[i]
        else:
            album[genres[i]] = plays[i]
    print(album)
    return answer

solution(['classic', 'pop', 'classic', 'classic', 'pop'],[500, 600, 150, 800, 2500])