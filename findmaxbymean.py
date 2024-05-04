#Goal: Determine largest number out of inputs by taking mean, removing all numbers less than mean, and continuing to do this until there is only one number left
def take_init_values():
  table = []
  length = input("How many numbers would you like to test: ")
  for num in range(1, int(length) + 1):
    text = "Enter value number " + str(num) + ": "
    new_value = int(input(text))
    table.append(new_value)
  return table


init_values = take_init_values()
print("Initial values:", init_values)
def take_mean(table):
  total = 0
  for num in table:
    total += num
  mean = total / len(table)
  print("Mean of current table:", mean)
  return mean

avg = take_mean(init_values)


def test(table):
  if (len(table) > 1) and (table[0] == table[1]):
    print("You have identical values for the largest number, it is", table[0])
  elif len(table) > 1:
    print("Table has", len(table), "values")
    new_mean = take_mean(table)
    remove_lower(table, new_mean)
  elif len(table) == 1:
    return True

def remove_lower(table, mean = avg):
  new_table = [num for num in table if num > mean]
  print("Removing values under mean, new table: " + str(new_table))
  if test(new_table):
    print("Only the largest number is left, it is", new_table[0])


remove_lower(init_values)

