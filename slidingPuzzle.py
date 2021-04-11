neighbor = [{1,4},{0,2,5},{1,3,6},{2,7},{0,5,8},{1,4,6,9},{2,5,7,10},
            {3,6,11},{4,9,12},{5,8,10,13},{6,9,11,14},{7,10,15},{8,13},{9,12,14},{10,13,15},{11,14}]

def swap(mat, i, j):
    newMat = mat.copy()
    temp = newMat[i]
    newMat[i] = newMat[j]
    newMat[j] = temp
    return newMat

def dfsSearch(mat):
    start = []
    for i in range(4):
        for j in range(4):
            start.append( str(mat[i][j]))
            
    queue = [start]
    visited = {str(start)}
    step = 0
    
    while queue != []:
        for i in range(len(queue)):
            cur = queue[0]
            for i in range(4):
                for j in range(4):
                    print(cur[4*i + j],end="  ")
                print()
            print()
                    
            
            
            queue = queue[1:]
            
            if cur == ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","0","0"]:
                return step
            
            pos1 = 0
            while cur[pos1] != "0":
                pos1 += 1
            
            pos2 = pos1 + 1
            while cur[pos2] != "0":
                pos2 += 1

            nb1 = neighbor[pos1]

            nb2 = neighbor[pos2]

            
            for nb in nb1:
                newState = swap(cur, pos1, nb)
                if str(newState) not in visited:
                    queue.append(newState)
                    visited.add(str(newState))
            
            for nb in nb2:
                newState = swap(cur, pos2, nb)
                if str(newState) not in visited:
                    queue.append(newState)
                    visited.add(str(newState))
                
        step += 1
        
    print("Not found")
        
matrix1 = [[1,0,2,4],[5,6,3,8],[9,10,0,12],[13,14,7,11]]
print(dfsSearch(matrix1))
    