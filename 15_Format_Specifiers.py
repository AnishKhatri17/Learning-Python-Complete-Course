"""
format specifiers = {value: flags} format a value based on what flags are inserted 

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place signn to leftmost position
# :  = insert a space before positive numbers
# :, = comma seperator
 
"""

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is Rs.{price1:.2f}")
print(f"Price 2 is Rs.{price2:.2f}")
print(f"Price 3 is Rs.{price3:.2f}")
print('\n')

#10 spaces allocation
print(f"Price 1 is Rs.{price1:10}")
print(f"Price 2 is Rs.{price2:10}")
print(f"Price 3 is Rs.{price3:10}")
print("\n")

#0 padded with 10 spaces
print(f"Price 1 is Rs.{price1:010}")
print(f"Price 2 is Rs.{price2:010}")
print(f"Price 3 is Rs.{price3:010}")
print("\n")

#left justified
print(f"Price 1 is Rs.{price1:<10}")
print(f"Price 2 is Rs.{price2:<10}")
print(f"Price 3 is Rs.{price3:<10}")
print("\n")

#right justified
print(f"Price 1 is Rs.{price1:>10}")
print(f"Price 2 is Rs.{price2:>10}")
print(f"Price 3 is Rs.{price3:>10}")
print("\n")

#center align
print(f"Price 1 is Rs.{price1:^10}")
print(f"Price 2 is Rs.{price2:^10}")
print(f"Price 3 is Rs.{price3:^10}")
print("\n")

#any positive numbers with be + started
print(f"Price 1 is Rs.{price1:+}")
print(f"Price 2 is Rs.{price2:+}")
print(f"Price 3 is Rs.{price3:+}")
print("\n")

#seperate with space in the beginning
print(f"Price 1 is Rs.{price1: }")
print(f"Price 2 is Rs.{price2: }")
print(f"Price 3 is Rs.{price3: }")
print("\n")

#thousand , seperator
print(f"Price 1 is Rs.{price1:+,.2f}")
print(f"Price 2 is Rs.{price2:+,.2f}")
print(f"Price 3 is Rs.{price3:+,.2f}")
print("\n")