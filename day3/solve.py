import re

input_file = open("input.txt", "r")

valid_muls = []

for line in input_file:
  line_valid_muls = re.findall("mul\(\d+\,\d+\)", line)
  valid_muls.extend(line_valid_muls)


total_result = 0
for valid_mul in valid_muls:
  mul_values = valid_mul[4:len(valid_mul)-1]
#  print(mul_values)
  values_str = mul_values.split(',')
  mul_result = int(values_str[0]) * int(values_str[1])
  total_result += mul_result

print(total_result)
