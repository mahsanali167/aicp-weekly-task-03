# Initialize an empty dictionary to store cow data
cow_data = {}

# Prompt the user for input
while True:
    try:
        cow_id = int(input("Enter the 3-digit cow identity code (0 to exit): "))
        if cow_id == 0:
            break  # Exit loop if user enters 0
        yield_today = float(input(f"Enter the milk yield for cow {cow_id} today (litres): "))

        # Store data in the dictionary
        if cow_id not in cow_data:
            cow_data[cow_id] = []
        cow_data[cow_id].append(yield_today)
    except ValueError:
        print("Invalid input. Please enter a valid cow ID and yield.")

print("\nYield data recorded successfully!\n")

# Calculate total weekly volume and average yield
total_volume = sum(sum(yields) for yields in cow_data.values())
num_cows = len(cow_data)
average_yield = total_volume / num_cows

# Display results
print(f"Total weekly volume of milk for the herd: {int(total_volume)} litres")
print(f"Average yield per cow in a week: {int(average_yield)} litres")

# Find the cow with the highest total yield
max_yield_cow = max(cow_data, key=lambda cow: sum(cow_data[cow]))

# Identify low-yield cows
low_yield_cows = [cow for cow in cow_data if sum(cow_data[cow]) < 12 * 4]

# Display results
print(f"\nMost productive cow (ID {max_yield_cow}):")
print(f"Weekly yield: {sum(cow_data[max_yield_cow]):.1f} litres")

print("\nCows with low yield (less than 12 litres on 4 or more days):")
for cow in low_yield_cows:
    print(f"Cow {cow}: Weekly yield: {sum(cow_data[cow]):.1f} litres")


