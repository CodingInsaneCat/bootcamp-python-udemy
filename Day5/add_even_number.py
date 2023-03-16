is_even_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        is_even_sum = is_even_sum + i

print(f"The total of the sum of evens numbers is {is_even_sum}")
