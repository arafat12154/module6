def calculate_unit_price(diameter, price):
    radius = diameter / 2
    area_cm2 = 3.14159265 * radius**2
    area_m2 = area_cm2 / 10000
    unit_price = price / area_m2
    return unit_price
if __name__ == "__main":
    print("Enter the details for the first pizza:")
    diameter1 = float(input("Diameter (in centimeters): "))
    price1 = float(input("Price (in euros): "))

    print("\nEnter the details for the second pizza:")
    diameter2 = float(input("Diameter (in centimeters): "))
    price2 = float(input("Price (in euros): "))

    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)

    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money.")
    elif unit_price2 < unit_price1:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas have the same unit price.")
