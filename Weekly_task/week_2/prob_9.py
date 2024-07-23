"""
City
"""
city = input("Enter the city: ")
if city.lower() == 'delhi':
    print(f"Monument in {city} is Red fort")
elif city.lower() == 'agra':
    print(f"Monument in {city} is Taj Mahal")
elif city.lower() == 'jaipur':
    print(f"Monument in {city} is Jal Mahal")
else:
    print(f"Invalid Input")