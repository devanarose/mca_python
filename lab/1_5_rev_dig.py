def is_palindrome(num):

  reversed_num = int(str(num)[::-1])
  return num == reversed_num

def reverse_and_add(num):

  while True:
    reversed_num = int(str(num)[::-1])
    sum_of_digits = num + reversed_num
    if is_palindrome(sum_of_digits):
      return sum_of_digits
    else:
      num = sum_of_digits

# Example usage
number = int(input("Enter number : "))
result = reverse_and_add(number)
if result != -1:
  print(f"The number {number} becomes a palindrome after reversing and adding digits: {result}")
else:
  print(f"The process for number {number} doesn't terminate with a palindrome.")
