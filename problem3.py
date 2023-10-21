def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters
while True:
    gallons = float(input("Enter a volume in American gallons (or a negative value to exit): "))

    if gallons < 0:
        print("Exiting the program.")
        break
    liters = gallons_to_liters(gallons)
    print(f"{gallons} gallons is approximately equal to {liters} liters.")
