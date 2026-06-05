print("===== PowerTrack =====")

total_units = 0
highest_units = 0
highest_appliance = ""

n = int(input("How many appliances do you want to enter? "))

for i in range(n):
    print("\nAppliance", i + 1)

    name = input("Enter appliance name: ")
    power = float(input("Power in watts: "))
    hours = float(input("Hours used per day: "))

    units = (power * hours) / 1000

    print("Daily usage =", round(units, 2), "kWh")

    total_units += units

    if units > highest_units:
        highest_units = units
        highest_appliance = name

monthly_units = total_units * 30

rate = float(input("\nEnter electricity rate (₹ per unit): "))

bill = monthly_units * rate

print("\n========== REPORT ==========")
print("Daily Energy Usage   :", round(total_units, 2), "kWh")
print("Monthly Energy Usage :", round(monthly_units, 2), "kWh")
print("Estimated Bill       : ₹", round(bill, 2))

print("\nHighest Energy Consumer:")
print(highest_appliance, "-", round(highest_units, 2), "kWh/day")

print("\nBill Category:")

if bill < 500:
    print("Low Electricity Usage")
elif bill < 1500:
    print("Moderate Electricity Usage")
else:
    print("High Electricity Usage")

print("\nEnergy Saving Tips")

if monthly_units > 300:
    print("- Switch off unused appliances")
    print("- Use LED bulbs")
    print("- Avoid standby mode")
elif monthly_units > 150:
    print("- Reduce unnecessary appliance usage")
    print("- Use energy-efficient devices")
else:
    print("- Yeahhh you saved moneyy")

print("\nThank you for using PowerTrack!")