import math

def splitPuzzleInput(input_file):
  rules=[]
  page_orderings=[]
  is_rules_section =True
  for line in input_file:
    if len(line) == 1 :
      is_rules_section = False
      continue

    if line[len(line)-1] =='\n': line = line[:len(line)-1] #removing '\n'

    if is_rules_section:
      rules.append(line.split('|'))
    else:
      page_orderings.append(line.split(','))
  return rules, page_orderings



def pertinentRules(rules, page_ordering):

  pertinent_rules = rules.copy()
  for rule in rules:
    if page_ordering.count(rule[0]) == 0 or page_ordering.count(rule[1]) == 0:
      pertinent_rules.remove(rule)

  return pertinent_rules

def isPageOrderingInRightOrder(page_ordering, rules):

  rules_cleaned = pertinentRules(rules, page_ordering)

  for page in page_ordering:
    rules_to_go_through = rules_cleaned.copy()
    for rule in rules_to_go_through:
      if page == rule[1]:
        return False
      elif page == rule[0]:
        rules_cleaned.remove(rule)

  return True

def rulesWithoutPage(rules, page):

  rules_without_page = rules.copy()
  for rule in rules:
    if page == rule[0] or page == rule[1]:
      rules_without_page.remove(rule)

  return rules_without_page

def firstPage(page_ordering, rules):
  for page in page_ordering:
    is_first = True
    for rule in rules:
      if page == rule[1]:
        is_first = False
        break
    if is_first : return page

  return -1

input_file = open("input.txt", "r")
rules, page_orderings = splitPuzzleInput(input_file)

result=0
page_ordering_wrongs = []
for page_ordering in page_orderings:
  if isPageOrderingInRightOrder(page_ordering, rules):
    middle_page_number = page_ordering[math.floor(len(page_ordering)/2)]
    result+=int(middle_page_number)
  else:
    page_ordering_wrongs.append(page_ordering)



print('Part 1 result : ',result, 'expecting 5732')

result_part2=0

for page_ordering_wrong in page_ordering_wrongs:
  rules_cleaned = pertinentRules(rules, page_ordering_wrong)

  page_ordering = page_ordering_wrong.copy()

  page_new_ordering = []
  rules_without_page = rules_cleaned

  while(len(page_ordering) > 0):
    first_page = firstPage(page_ordering, rules_without_page)
    page_ordering.remove(first_page)
    page_new_ordering.append(first_page)
    rules_without_page = rulesWithoutPage(rules_without_page, first_page)

  result_part2 += int(page_new_ordering[math.floor(len(page_new_ordering)/2)])

print('Part 2 result : ',result_part2, 'expecting 4716')