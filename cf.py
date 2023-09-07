

# temperature in Fahrenheit and Celsius program

# assume fahrenheit is float
def convert_f_to_c(fahrenheit):
    celsius = float(fahrenheit - 32) * 5 / 9
    return celsius

# assume celsius is float
def convert_c_to_f(celsius):
    fahrenheit = float(celsius) * 9 / 5 + 32
    return fahrenheit

temp = input('Input temperature  ')
symbol = input('Input Scale (F or C)? ')

print('======================')

if (symbol == 'F'):
    print('So the temperature is')
    print('Faharenheit:' + temp )
    print('Celsius:' + str(convert_f_to_c(float(temp))) )
elif (symbol == 'C'):
    print('So the temperature is')
    print('Faharenheit:' + str(convert_c_to_f(float(temp))) )
    print('Celsius:' + temp )
else:
    print("Please use F or C for scale")




