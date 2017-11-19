input_rod_dist = float(input("Enter the distance in rods: "))

dist_meters = input_rod_dist * 5.0292
dist_furlong = input_rod_dist / 40
dist_miles = dist_meters / 1609.34

print("Your input: ", input_rod_dist)
print("\nConversions")
print("Meters: ", dist_meters)
print("Furlong: ", dist_furlong)
print("Miles: ", dist_miles)
print("Feet: ", dist_meters/ 0.3048)

print('Time to walk {} rods in Minutes: '.format(input_rod_dist), (dist_miles * 60) / 3.1)