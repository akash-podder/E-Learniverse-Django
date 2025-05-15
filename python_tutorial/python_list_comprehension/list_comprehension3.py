# Double For Loop
matrix = [[1,2,3],[4,5,6],[7,8,9]]

new_matrix = []

# Flattening the Matrix from 2D to 1D
for row in matrix:
    for num in row:
        new_matrix.append(num)

print(new_matrix)

# List Comprehension
# [x for 1ST For Loop 2ND For Loop]
new_list = [num for row in matrix for num in row]
print(new_list)