#test calculator code, non graphical

num1 = int(input("Enter first number: "))

while True:
    operation = input("Enter operation: ")

    if operation == "STOP":
        print("Calculator stopped.")
        break

    if operation == "=":
        print("Result:", num1)
        continue

    if operation not in ["+", "-", "*", "/", "%"]:
        print("Invalid operation")
        continue

    num2 = int(input("Enter next number: "))

    if operation == "+":
        num1 = num1 + num2
    elif operation == "-":
        num1 = num1 - num2
    elif operation == "*":
        num1 = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error: Division by zero!")
            continue
        num1 = num1 / num2
    elif operation == "%":
        num1 = num1 % num2  # modulus calc, not percentage


# Step 1 - Add a tkinter import to make screen resemble a calculator
# Step 2 - Integrate unit convertor from previous project - make like a calculator app
# Step 3 - Make a separate visual display for unit convertor
# Step 4 - General customisation

#Unit convertor

# print("Welcome to Unit Convertor :\n 1. Length \n2. Weight \n3. Temperature\n4. Speed\n\n Select the type of conversion you want to perform (1-4): ")
# choice=int(input("Enter : "))
# if choice==1: # Length conversion
#     print("You have selected Length conversion")
#     print("1. Meter to Kilometer \n2. Kilometer to Meter \n3. Meter to Centimeter \n4. Centimeter to Meter \n5. Kilometer to Centimeter \n6. Centimeter to Kilometer")
#     length_choice=int(input("Enter your choice (1-6): "))
#     if length_choice==1: 
#         meter=float(input("Enter length in metres: "))
#         kilometer=meter/1000
#         print(f"{meter} metres is equal to {kilometer} kilometers")
#     elif length_choice==2:
#         kilometer=float(input("Enter length in kilometers: "))
#         meter=kilometer*1000
#         print(f"{kilometer} kilometers is equal to {meter} metres")
#     elif length_choice==3:
#         meter=float(input("Enter length in metres: "))
#         centimeter=meter*100
#         print(f"{meter} metres is equal to {centimeter} centimeters")
#     elif length_choice==4:
#         centimeter=float(input("Enter length in centimeters: "))
#         meter=centimeter/100
#         print(f"{centimeter} centimeters is equal to {meter} metres")
#     elif length_choice==5:
#         kilometer=float(input("Enter length in kilometers: "))
#         centimeter=kilometer*100000
#         print(f"{kilometer} kilometers is equal to {centimeter} centimeters")
#     elif length_choice==6:
#         centimeter=float(input("Enter length in centimeters: "))
#         kilometer=centimeter/100000
#         print(f"{centimeter} centimeters is equal to {kilometer} kilometers")
#     else:
#         print("Invalid choice")
# elif choice==2: # Weight conversion
#     print("You have selected Weight conversion")
#     print("1. Kilogram to Gram \n2. Gram to Kilogram \n3. Kilogram to Milligram \n4. Milligram to Kilogram \n5. Gram to Milligram \n6. Milligram to Gram")
#     weight_choice=int(input("Enter your choice (1-6): "))
#     if weight_choice==1:
#         kilogram=float(input("Enter weight in kilograms: "))
#         gram=kilogram*1000
#         print(f"{kilogram} kilograms is equal to {gram} grams")
#     elif weight_choice==2:
#         gram=float(input("Enter weight in grams: "))
#         kilogram=gram/1000
#         print(f"{gram} grams is equal to {kilogram} kilograms")
#     elif weight_choice==3:
#         kilogram=float(input("Enter weight in kilograms: "))
#         milligram=kilogram*1000000
#         print(f"{kilogram} kilograms is equal to {milligram} milligrams")
#     elif weight_choice==4:
#         milligram=float(input("Enter weight in milligrams: "))
#         kilogram=milligram/1000000
#         print(f"{milligram} milligrams is equal to {kilogram} kilograms")
#     elif weight_choice==5:
#         gram=float(input("Enter weight in grams: "))
#         milligram=gram*1000
#         print(f"{gram} grams is equal to {milligram} milligrams")
#     elif weight_choice==6:
#         milligram=float(input("Enter weight in milligrams: "))
#         gram=milligram/1000
#         print(f"{milligram} milligrams is equal to {gram} grams")
#     else:
#         print("Invalid choice")
# elif choice==3: # Temperature conversion
#     print("You have selected Temperature conversion")
#     print("1. Celsius to Fahrenheit \n2. Fahrenheit to Celsius \n3. Celsius to Kelvin \n4. Kelvin to Celsius \n5. Fahrenheit to Kelvin \n6. Kelvin to Fahrenheit")
#     temp_choice=int(input("Enter your choice (1-6): "))
#     if temp_choice==1:
#         celsius=float(input("Enter temperature in Celsius: "))
#         fahrenheit=(celsius*9/5)+32
#         print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")
#     elif temp_choice==2:
#         fahrenheit=float(input("Enter temperature in Fahrenheit: "))
#         celsius=(fahrenheit-32)*5/9
#         print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")
#     elif temp_choice==3:
#         celsius=float(input("Enter temperature in Celsius: "))
#         kelvin=celsius+273.15
#         print(f"{celsius} Celsius is equal to {kelvin} Kelvin")
#     elif temp_choice==4:    
#         kelvin=float(input("Enter temperature in Kelvin: "))
#         celsius=kelvin-273.15
#         print(f"{kelvin} Kelvin is equal to {celsius} Celsius")
#     elif temp_choice==5:
#         fahrenheit=float(input("Enter temperature in Fahrenheit: "))
#         kelvin=(fahrenheit-32)*5/9+273.15
#         print(f"{fahrenheit} Fahrenheit is equal to {kelvin} Kelvin")
#     elif temp_choice==6:
#         kelvin=float(input("Enter temperature in Kelvin: "))
#         fahrenheit=(kelvin-273.15)*9/5+32
#         print(f"{kelvin} Kelvin is equal to {fahrenheit} Fahrenheit")
#     else:
#         print("Invalid choice")
# elif choice==4: # Speed conversion
#     print("You have selected Speed conversion")
#     print("1. Kilometer per hour to Meter per second \n2. Meter per second to Kilometer per hour \n3. Mile per hour to Kilometer per hour \n4. Kilometer per hour to Mile per hour \n5. Mile per hour to Meter per second \n6. Meter per second to Mile per hour")
#     speed_choice=int(input("Enter your choice (1-6): "))
#     if speed_choice==1:
#         kmph=float(input("Enter speed in Kilometer per hour: "))
#         mps=kmph/3.6
#         print(f"{kmph} Kilometer per hour is equal to {mps} Meter per second")
#     elif speed_choice==2:
#         mps=float(input("Enter speed in Meter per second: "))
#         kmph=mps*3.6
#         print(f"{mps} Meter per second is equal to {kmph} Kilometer per hour")
#     elif speed_choice==3:
#         mph=float(input("Enter speed in Mile per hour: "))
#         kmph=mph*1.60934
#         print(f"{mph} Mile per hour is equal to {kmph} Kilometer per hour")
#     elif speed_choice==4:
#         kmph=float(input("Enter speed in Kilometer per hour: "))
#         mph=kmph/1.60934
#         print(f"{kmph} Kilometer per hour is equal to {mph} Mile per hour")
#     elif speed_choice==5:
#         mph=float(input("Enter speed in Mile per hour: "))
#         mps=mph*0.44704
#         print(f"{mph} Mile per hour is equal to {mps} Meter per second")
#     elif speed_choice==6:
#         mps=float(input("Enter speed in Meter per second: "))
#         mph=mps/0.44704
#         print(f"{mps} Meter per second is equal to {mph} Mile per hour")
#     else:
#         print("Invalid choice")
   
