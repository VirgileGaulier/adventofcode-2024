def isLevelSafe(diff, prev_diff):
  if abs(diff) < 1 or abs(diff) > 3: return False
  if prev_diff != 0:
    if diff > 0 and prev_diff < 0: return False
    if diff < 0 and prev_diff > 0: return False
  return True

input_file = open("input.txt", "r")
reports_safe = 0

for reports in input_file:
   prev_level = -1
   prev_diff = 0
   level_safe = True
   levels = reports.split()

   for level_str in levels:
     level = int(level_str)

     if prev_level == -1:
       prev_level = level
       continue

     diff = prev_level - level

     if isLevelSafe(diff, prev_diff) == False:
       level_safe = False
       break

     prev_diff = diff
     prev_level = level

   if level_safe:
     reports_safe +=1

print(reports_safe)