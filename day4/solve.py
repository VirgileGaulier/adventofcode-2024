import re
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

horizontal_lines = []
for y in range(matrix_max_y):
  line =''
  for x in range(matrix_max_x):
    char = matrix[y][x]
    line += char
  horizontal_lines.append(line)


vertical_lines = []
for x in range(matrix_max_x):
  line =''
  for y in range(matrix_max_y):
    char = matrix[y][x]
    line += char
  vertical_lines.append(line)


diagonal_start = []
for y in sorted(range(matrix_max_y-3),reverse=True):
  diagonal_start.append([0,y])

for x in range(1, matrix_max_x-3):
  diagonal_start.append([x,0])

diagonal_lines = []
for start in diagonal_start:
  x = start[0]
  y = start[1]
  line =''
  while x < matrix_max_x and y < matrix_max_y:
    char = matrix[y][x]
    line += char
    x += 1
    y += 1
  diagonal_lines.append(line)

diagonal_start_reverse = []

for x in range(3, matrix_max_x):
  diagonal_start_reverse.append([x,0])

for y in sorted(range(1, matrix_max_y-3)):
  diagonal_start_reverse.append([matrix_max_x-1,y])

diagonal_reverse_lines = []
for start in diagonal_start_reverse:
  x = start[0]
  y = start[1]
  line =''
  while x >= 0 and y < matrix_max_y:
    char = matrix[y][x]
    line += char
    x -= 1
    y += 1
  diagonal_reverse_lines.append(line)

all_lines = []
all_lines.extend(horizontal_lines)
all_lines.extend(vertical_lines)
all_lines.extend(diagonal_lines)
all_lines.extend(diagonal_reverse_lines)


total = 0
for line in all_lines:
  rw = re.findall(XMAS_word, line)
  rwr = re.findall(XMAS_word_revert, line)
  r_count = len(rw) + len(rwr)
  print(line, r_count)
  total += r_count

print("total",total ,"expecting 2662")
