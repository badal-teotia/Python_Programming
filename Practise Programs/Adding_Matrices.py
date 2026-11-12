# Adding matrices.

A = ([1,3,6],
     [4,6,8],
     [2,7,8])

B = ([3,6,5],
     [9,8,7],
     [1,2,6])

result = ([0,0,0],
          [0,0,0],
          [0,0,0])

for i in range(0,3):
    for j in range(0,3):
        result[i][j] = A[i][j] + B[i][j]
        
for l in range(0,3):
    print(result[l])
    