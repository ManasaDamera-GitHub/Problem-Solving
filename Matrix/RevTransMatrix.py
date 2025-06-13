matrix=[[1,2,3],      #[7,4,1],
        [4,5,6],      #[8,5,2],
        [7,8,9]]      #[9,6,3]   3*3 matrix
rows=len(matrix)
cols=len(matrix[0])
output=[]
for i in range(cols):
    rev=[]
    for j in range(rows-1,-1,-1):
        rev.append(matrix[j][i])
    output.append(rev)
print(output)


# using reverse() method:
# -------------------------
# matrix=[[1,2,3],      #[7,4,1],
#         [4,5,6],      #[8,5,2],
#         [7,8,9]]      #[9,6,3]
# rows=len(matrix)
# cols=len(matrix[0])
# output=[]
# for i in range(cols):
#     rev=[]
#     for j in range(rows):
#         rev.append(matrix[j][i])
#     output.append(rev)
# for row in output:
#     row.reverse()
# print(output)