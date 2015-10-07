#This program takes a farenheit input and converts it to celsius

farenheit_input = input("Input temperature in farenheit\n")
farenheit_input = int(farenheit_input)
celsius_output = (farenheit_input - 32) / 1.8

print(celsius_output)
