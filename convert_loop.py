#convert_loop.py
# A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    celsius1, celsius2, celsius3, celsius4, celsius5 = eval(input("Please enter five temperatures in Celsius(separated by comma) that you would like to convert to Fahrenheit "))
    CelsiusList = list([celsius1, celsius2, celsius3, celsius4, celsius5])
    for i in CelsiusList:
        fahrenheit = 9/5 * celsius + 32
    
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    
main()