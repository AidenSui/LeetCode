def candy(ratings) -> int:
    dist = []
    for i in range(len(ratings)):
        if i > 0 and ratings[i] > ratings[i-1]:
            count = dist[i-1] + 1
        else: 
            count = 1
        dist.append(count)
        
    print(dist)
    
    for i in range(len(ratings)-1, -1, -1):
        if i < len(ratings) - 1 and ratings[i] > ratings[i+1]:
            if dist[i] <= dist[i+1]:
                dist[i] = dist[i+1] + 1
            
    print(dist)
    
    return sum(dist)

print(candy([1,2,87,87,87,2,1]))