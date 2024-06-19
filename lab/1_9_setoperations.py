# Perform various set operations
#     Set Union
#     Set Intersection
#     Set Difference

def main():

  set1 = {1, 3, 5, 7}
  set2 = {2, 4, 6, 8, 10}

  # Union 
  union_set = set1 | set2
  print("Union:", union_set)

  # Intersection 
  intersection_set = set1 & set2
  print("Intersection:", intersection_set)

  # Difference 
  difference_set = set1 - set2
  print("Difference (set1 - set2):", difference_set)

  # Difference 
  difference_set = set2.difference(set1)
  print("Difference (set2 - set1):", difference_set)

if __name__ == "__main__":
  main()
