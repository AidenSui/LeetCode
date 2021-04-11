def swap(mat, i, j):
    newMat = mat.copy()
    temp = newMat[i]
    newMat[i] = newMat[j]
    newMat[j] = temp
    return newMat

m1 = [1,2,3,4,5,6]
m1 = swap(m1, 2, 4)
print(m1)