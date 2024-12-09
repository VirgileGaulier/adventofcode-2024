input_file = open("input.txt", "r")

tests = []

for line in input_file:
  if line[len(line)-1] =='\n': line = line[:len(line)-1] #removing '\n'
  s = line.split(':')
  result = s[0]
  equation = s[1].strip().split(' ')
  tests.append({ 'result' : result, 'eq':equation})

tests_solvable = 0

for test in tests:
  print(test)
  eq = test['eq']
  for i in range(pow(2,len(eq)-1)):
    r = int(eq[0])
    r_str = ' '+str(r)
    for u in range(0, len(eq)-1):
      if (i >> u & 1) == 1:
        r = r * int(eq[u+1])
        r_str += ' * '+eq[u+1]
      else:
        r = r + int(eq[u+1])
        r_str += ' + '+eq[u+1]

    #print(r)
    #print(r_str)
    if r == int(test['result']):
      tests_solvable+=r
      break

print("tests_solvable", tests_solvable)