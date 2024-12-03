def isLevelSafe(diff, prev_diff):
  if abs(diff) < 1 or abs(diff) > 3: return False
  if prev_diff != 0:
    if diff > 0 and prev_diff < 0: return False
    if diff < 0 and prev_diff > 0: return False
  return True


def isReportSafe(levels):
  prev_level = -1
  prev_diff = 0

  for level_str in levels:
    level = int(level_str)

    if prev_level == -1:
       prev_level = level
       continue

    diff = prev_level - level

    if isLevelSafe(diff, prev_diff) == False:
      return False

    prev_diff = diff
    prev_level = level

  return True



input_file = open("input.txt", "r")
reports_safe = 0
reports_safe_with_one_error = 0

for report in input_file:

   levels = report.split()

   if isReportSafe(levels):
     reports_safe +=1
     reports_safe_with_one_error+=1
     continue

   #brute force ... look if with one element removed it's working...
   for i in range(len(levels)):
     level_copy = levels.copy()
     level_copy.pop(i)
     if isReportSafe(level_copy):
       reports_safe_with_one_error +=1
       break


print("reports_safe",reports_safe)
print("reports_safe_with_one_error",reports_safe_with_one_error)