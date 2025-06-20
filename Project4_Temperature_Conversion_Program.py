# Temperature Conversion Program

unit = input("Is this temperature is Celcius and Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print("\n")
    print(f"The temperature in Fahrenheit is: {temp}°F")

elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print("\n")
    print(f"The temperature in Celcius is: {temp}°C")

else:
    print(f"{unit} is an invalid unit of measurement.")