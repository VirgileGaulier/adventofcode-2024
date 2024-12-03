list_1 = []
list_2 = []

input_file = open("input.txt", "r")
for line in input_file:
  line_splitted = line.split()
  list_1.append(int(line_splitted[0]))
  list_2.append(int(line_splitted[1]))

list_1.sort()
list_2.sort()

i=0
total_distance = 0
for list_1_value in list_1:
    distance = abs(list_1_value - list_2[i])
    i += 1
    total_distance+= distance

print("total_distance : ",total_distance)

similarity_score = 0
for list_1_value in list_1:
  for list_2_value in list_2:
    if list_1_value == list_2_value:
      similarity_score += list_1_value

print("similarity_score : ",similarity_score)