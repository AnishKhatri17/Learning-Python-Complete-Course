# indexing = accessign elements os a sequence using [] (indexing operator)
#            [start : end : stop]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[7])
print(credit_number[10])
#printing first 4 digits
print(credit_number[:4]) 
print(credit_number[0:4]) # first is inclusive and last is exclusive
print(credit_number[5:9]) 
print(credit_number[5:]) # everyhing after the index 5 (inclusive).
#we can also use negative index
print(credit_number[-5])
print(credit_number[-1]) # -1 is the last character

print(credit_number[::2]) # this will print every second character 
print(credit_number[::3]) # this will print every third character 


last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

#reverse the character of the string
reverse = credit_number[::-1]
print("\n"+f"The reversed credit card is: {reverse}")