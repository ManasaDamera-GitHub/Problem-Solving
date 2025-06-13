matrix=[[1,2,3],      #[1,4,7],
        [4,5,6],      #[2,5,8],
        [7,8,9]]      #[3,6,9]
rows=len(matrix)
cols=len(matrix[0])
output=[]
for i in range(cols):
    new=[]
    for j in range(rows):
        new.append(matrix[j][i])
    output.append(new)
print(output)


