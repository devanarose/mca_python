# Write a program to find the number and sum of all integers greater than 100
# and less than 200 that are divisible by 7.

count = 0
total_sum = 0

for num in range(101, 200):
  if num % 7 == 0:
    count += 1
    total_sum += num

print(f"Number of integers divisible by 7: {count}")
print(f"Sum of integers divisible by 7: {total_sum}")
