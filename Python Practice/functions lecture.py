def fahrenheitToCelsius(t):
    convertedTemperature=(5/9) * (t-32)
    return convertedTemperature

fahrenheitTemp=eval(input('Enter a temperature in degrees Fahrenheit: '))
celsiusTemp=fahrenheitToCelsius(fahrenheitTemp)
print('celsius equivalent: ', celsiusTemp, 'degrees')
                    
