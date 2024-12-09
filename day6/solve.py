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

def isGuardInRange(x, y, d, matrix):
  if x <= 0 and d == 'W':
    return False
  if x >= (len(matrix)-1) and d == 'E':
    return False
  if y <= 0 and d == 'N':
    return False
  if y >= (len(matrix)-1) and d == 'S':
    return False
  return True

def nextPosition(q_x, q_y, q_d):
  if q_d == 'N':
    return q_x, q_y-1
  elif q_d == 'S':
     return q_x, q_y+1
  elif q_d == 'E':
    return q_x+1, q_y
  elif q_d == 'W':
     return q_x-1, q_y

def rotateDirection(q_d):
  if q_d == 'N':
    return 'E'
  elif q_d == 'S':
    return 'W'
  elif q_d == 'E':
    return 'S'
  elif q_d == 'W':
    return 'N'

import copy
input_file = open("input.txt", "r")

matrix = []
y=0
for line in input_file:
  if line[len(line)-1] =='\n': line = line[:len(line)-1] #removing '\n'

  matrix.append([])
  for x in range(len(line)):
    matrix[y].append(line[x])
  y+=1

print(matrix)

guard_first_position = findGuardFirstPosition(matrix)
guard_position = guard_first_position
print("guard_first_position", guard_first_position)

q_x = guard_position[0]
q_y = guard_position[1]
q_d = guard_position[2]
visited = {str(q_x)+"-"+str(q_y) : True}
has_moved = False

while(isGuardInRange(q_x, q_y, q_d, matrix)):
  next_x, next_y = nextPosition(q_x, q_y, q_d)
  next_place =  matrix[next_y][next_x]
  if next_place == '#' :
    q_d = rotateDirection(q_d)
  else:
    q_x = next_x
    q_y = next_y

  visited[str(q_x)+"-"+str(q_y)] = True

print('result:',len(visited),' expecting 5208')



##Part 2
loop_count =0

for obstruction_x in range(len(matrix)):
  for obstruction_y in range(len(matrix)):
    if obstruction_x == guard_first_position[0] and obstruction_y == guard_first_position[1]:
      continue
    if matrix[obstruction_y][obstruction_x] == '#':
      continue

    matrix_with_new_obstruction = copy.deepcopy(matrix)
    matrix_with_new_obstruction[obstruction_y][obstruction_x] = '#'
    
    q_x = guard_first_position[0]
    q_y = guard_first_position[1]
    q_d = guard_first_position[2]
    visited_in_same_direction = {str(q_x)+'-'+str(q_y)+'-'+str(q_d) : True}

    while(isGuardInRange(q_x, q_y, q_d, matrix_with_new_obstruction)):
      next_x, next_y = nextPosition(q_x, q_y, q_d)
      next_place =  matrix_with_new_obstruction[next_y][next_x]

      if next_place == '#' :
        q_d = rotateDirection(q_d)
      else:
        q_x = next_x
        q_y = next_y
      
      str_position = str(q_x)+'-'+str(q_y)+'-'+str(q_d)
      if str_position in visited_in_same_direction and visited_in_same_direction[str_position]:
        loop_count +=1
        break

      visited_in_same_direction[str_position]=True


print('result part 2 :',loop_count,' expecting 1972')