input_file = open("example.txt", "r")

matrix = []
for line in input_file:
  if line[len(line)-1] =='\n': line = line[:len(line)-1] #removing '\n'
  matrix.append(line)

print(matrix)


def findGuardFirstPosition(matrix):
  x = 0
  y = 0

  for line in matrix:
    for char in line:
      if char == '<':
        return x, y, 'W'
      if char == '>':
        return x, y, 'E'
      if char == '^':
        return x, y, 'N'
      if char =='v':
        return x, y, 'S'

      x+=1
    x=0
    y+=1

  return -1 , -1, 'U'


guard_first_position = findGuardFirstPosition(matrix)
guard_position = guard_first_position
print("guard_first_position", guard_first_position)


def isGuardInRange(x, y, d, matrix):
  if x == 0 and d == 'N':
    return False
  if x == len(matrix) and d == 'S':
    return False
  if y == 0 and d == 'W':
    return False
  if y == len(matrix) and d == 'E':
    return False
  return True

q_x = guard_position[0]
q_y = guard_position[1]
q_d = guard_position[2]
result =0

while(isGuardInRange(q_x, q_y, q_d, matrix)):
  if q_d == 'N':
    if not isGuardInRange(q_x, q_y-1, q_d, matrix) :break
    if matrix[q_y-1][q_x] == '#':
      q_d = 'E'
    else:
      q_y -=1
  elif q_d == 'E':
    if not isGuardInRange(q_x+1, q_y, q_d, matrix) :break
    if matrix[q_y][q_x+1] == '#':
      q_d = 'S'
    else:
      q_x +=1
  elif q_d == 'S':
    if not isGuardInRange(q_x, q_y+1, q_d, matrix) :break
    if matrix[q_y+1][q_x] == '#':
      q_d = 'W'
    else:
      q_y +=1
  elif q_d == 'W':
    if not isGuardInRange(q_x-1, q_y, q_d, matrix) :break
    if matrix[q_y][q_x-1] == '#':
      q_d = 'N'
    else:
      q_x -=1
  result+=1

print('result:',result,' expecting 41')