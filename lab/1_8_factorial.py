def factorial_memo(n, memo={}):
  if n in memo:
    return memo[n]
  elif n == 0:
    return 1
  else:
    result = n * factorial_memo(n-1, memo)
    memo[n] = result
    return result


number = int(input("enter the number : "))
factorial = factorial_memo(number)
print(f"Factorial of {number}: {factorial}")
