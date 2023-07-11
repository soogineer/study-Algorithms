def solution(wallpaper):
    c, r = [], [] 
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])): 
            if wallpaper[i][j] == "#": 
                c.append(i) 
                r.append(j) 
    return [min(c), min(r), max(c) + 1, max(r) + 1]