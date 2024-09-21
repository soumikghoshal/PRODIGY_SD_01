unit = int(input("Choose any one:\n1. Celsius to Fahrenheit\n2. Celsius to Kelvin\n3. Fahrenheit to Celsius\n4. Fahrenheit to Kelvin\n5. Kelvin to Celsius\n6. Kelvin to Fahrenheit\n"))

temp = float(input("Enter temperature: "))

if unit == 1:
    # Celsius to Fahrenheit
    result = (temp * 9/5) + 32
    print(f"{temp}°C is {result}°F")
elif unit == 2:
    # Celsius to Kelvin
    result = temp + 273.15
    print(f"{temp}°C is {result} K")
elif unit == 3:
    # Fahrenheit to Celsius
    result = (temp - 32) * 5/9
    print(f"{temp}°F is {result}°C")
elif unit == 4:
    # Fahrenheit to Kelvin
    result = (temp - 32) * 5/9 + 273.15
    print(f"{temp}°F is {result} K")
elif unit == 5:
    # Kelvin to Celsius
    result = temp - 273.15
    print(f"{temp} K is {result}°C")
elif unit == 6:
    # Kelvin to Fahrenheit
    result = (temp - 273.15) * 9/5 + 32
    print(f"{temp} K is {result}°F")
else:
    print("Invalid option selected.")
