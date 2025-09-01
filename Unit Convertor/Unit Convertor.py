#Unit convertor

print("Welcome to Unit Convertor :\n 1. Length \n2. Weight \n3. Temperature\n4. Speed\n\n Select the type of conversion you want to perform (1-4): ")
choice=int(input("Enter : "))
if choice==1: # Length conversion
    print("You have selected Length conversion")
    print("1. Meter to Kilometer \n2. Kilometer to Meter \n3. Meter to Centimeter \n4. Centimeter to Meter \n5. Kilometer to Centimeter \n6. Centimeter to Kilometer")
    length_choice=int(input("Enter your choice (1-6): "))
    if length_choice==1: 
        meter=float(input("Enter length in metres: "))
        kilometer=meter/1000
        print(f"{meter} metres is equal to {kilometer} kilometers")
    elif length_choice==2:
        kilometer=float(input("Enter length in kilometers: "))
        meter=kilometer*1000
        print(f"{kilometer} kilometers is equal to {meter} metres")
    elif length_choice==3:
        meter=float(input("Enter length in metres: "))
        centimeter=meter*100
        print(f"{meter} metres is equal to {centimeter} centimeters")
    elif length_choice==4:
        centimeter=float(input("Enter length in centimeters: "))
        meter=centimeter/100
        print(f"{centimeter} centimeters is equal to {meter} metres")
    elif length_choice==5:
        kilometer=float(input("Enter length in kilometers: "))
        centimeter=kilometer*100000
        print(f"{kilometer} kilometers is equal to {centimeter} centimeters")
    elif length_choice==6:
        centimeter=float(input("Enter length in centimeters: "))
        kilometer=centimeter/100000
        print(f"{centimeter} centimeters is equal to {kilometer} kilometers")
    else:
        print("Invalid choice")
elif choice==2: # Weight conversion
    print("You have selected Weight conversion")
    print("1. Kilogram to Gram \n2. Gram to Kilogram \n3. Kilogram to Milligram \n4. Milligram to Kilogram \n5. Gram to Milligram \n6. Milligram to Gram")
    weight_choice=int(input("Enter your choice (1-6): "))
    if weight_choice==1:
        kilogram=float(input("Enter weight in kilograms: "))
        gram=kilogram*1000
        print(f"{kilogram} kilograms is equal to {gram} grams")
    elif weight_choice==2:
        gram=float(input("Enter weight in grams: "))
        kilogram=gram/1000
        print(f"{gram} grams is equal to {kilogram} kilograms")
    elif weight_choice==3:
        kilogram=float(input("Enter weight in kilograms: "))
        milligram=kilogram*1000000
        print(f"{kilogram} kilograms is equal to {milligram} milligrams")
    elif weight_choice==4:
        milligram=float(input("Enter weight in milligrams: "))
        kilogram=milligram/1000000
        print(f"{milligram} milligrams is equal to {kilogram} kilograms")
    elif weight_choice==5:
        gram=float(input("Enter weight in grams: "))
        milligram=gram*1000
        print(f"{gram} grams is equal to {milligram} milligrams")
    elif weight_choice==6:
        milligram=float(input("Enter weight in milligrams: "))
        gram=milligram/1000
        print(f"{milligram} milligrams is equal to {gram} grams")
    else:
        print("Invalid choice")
