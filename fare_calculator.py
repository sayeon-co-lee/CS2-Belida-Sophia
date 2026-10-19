# Travel Fare Calculator
FARE_RATE = 14

# 1. Validate passenger name 
while True:
    name = input("Enter passenger name: ")
    if name.strip() != "":
        break
    print("Invalid name. Name cannot be empty. Please try again.")

# 2. Validate distance 
while True:
    distance_str = input("Enter distance (km): ")
    try:
        distance = float(distance_str)
        if distance > 0:
            break
        else:
            print("Invalid distance. Distance must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for distance.")

# 3. Validate number of passengers 
while True:
    passengers_str = input("Enter number of passengers: ")
    if passengers_str.isdigit():
        passengers = int(passengers_str)
        if passengers > 0:
            break
        else:
            print("Invalid number of passengers. Must be a positive whole number greater than 0.")
    else:
        print("Invalid input. Please enter a whole number.")

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
