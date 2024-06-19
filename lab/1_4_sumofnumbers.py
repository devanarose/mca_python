#Write a recursive function to calculate the sum of numbers from 0 to 10
def sum_to_n(n):

  if n == 0:
    return 0
  else:
    return n + sum_to_n(n - 1)

sum = sum_to_n(10)
print(f"The sum of numbers from 0 to 10 is: {sum}")
