'''
Even or Odd
'''
user_input = input("Enter numbers separated by spaces: ")
nums = __________(user_input.split())
evens = []
for n in nums:
    if n __________ 2 == 0:
        evens.append(n)
print("Even numbers:", evens)
