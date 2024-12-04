def isAAroundMas(matrix, x_a, y_a):
  top_left_corner_char = matrix[y_a-1][ x_a-1 ]
  top_right_corner_char = matrix[y_a-1][x_a+1]
  bottom_left_corner_char = matrix[y_a+1][x_a-1]
  bottom_right_corner_char = matrix[y_a+1][x_a+1]

  if top_left_corner_char == 'M' and top_right_corner_char == 'M' and bottom_left_corner_char == 'S' and bottom_right_corner_char == 'S':
    return True
  if top_left_corner_char == 'S' and top_right_corner_char == 'S' and bottom_left_corner_char == 'M' and bottom_right_corner_char == 'M':
    return True
  if top_left_corner_char == 'M' and top_right_corner_char == 'S' and bottom_left_corner_char == 'M' and bottom_right_corner_char == 'S':
    return True
  if top_left_corner_char == 'S' and top_right_corner_char == 'M' and bottom_left_corner_char == 'S' and bottom_right_corner_char == 'M':
    return True
  return False



input_file = open("input.txt", "r")

matrix = []
for line in input_file:
  matrix.append(line)


XMAS_word = 'XMAS'
XMAS_word_revert = 'SAMX'
matrix_max_x = len(matrix[0])-1 #remove endline char
matrix_max_y = len(matrix)

print("matrix_max_x", matrix_max_x)
print("matrix_max_y", matrix_max_y)

total = 0
for x in range(1, matrix_max_x-1):
  for y in range(1, matrix_max_y-1):
    if matrix[y][x] == 'A' and isAAroundMas(matrix, x, y):
      total+= 1

print(total)



