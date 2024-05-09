import csv
import random
from datetime import datetime, timedelta

# Marvel characters with associated fictional locations and product preferences
marvel_characters = {
    "Iron Man": {
        "location": "Stark Tower, New York",
        "preferences": {
            "electronics": ["Stark Industries", "Stark Tower Tech Store"],
            "luxury items": ["Stark Industries"],
            "dining": ["Avengers Tower Restaurant", "New York City Restaurants"]
        }
    },
    "Thor": {
        "location": "Asgard",
        "preferences": {
            "rare artifacts": ["Asgardian Antiques"],
            "weapons": ["Odin's Armory"],
            "dining": ["Asgardian Feasts"]
        }
    },
    "Spider-Man": {
        "location": "Queens, New York",
        "preferences": {
            "web-slinging equipment": ["Web-Shooters R Us"],
            "photography supplies": ["Daily Bugle Supplies"],
            "dining": ["Pizza Places", "Food Carts"]
        }
    },
    # Add more characters with their preferences and locations
}

# Function to generate synthetic dataset
def generate_synthetic_dataset():
    transactions = []
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 3, 31)
    current_date = start_date

    while current_date <= end_date:
        # Randomize timestamp within peak shopping hours
        timestamp = current_date + timedelta(hours=random.randint(10, 21), minutes=random.randint(0, 59), seconds=random.randint(0, 59))

        # Select a random Marvel character
        character = random.choice(list(marvel_characters.keys()))
        location = marvel_characters[character]["location"]

        # Randomize product and vendor based on character preferences
        product_type = random.choice(list(marvel_characters[character]["preferences"].keys()))
        vendor = random.choice(marvel_characters[character]["preferences"][product_type])

        # Dynamically generate transaction description
        if product_type == "electronics":
            description = f"{character} purchased {random.choice(['a', 'an'])} {random.choice(['smartphone', 'laptop', 'tablet', 'gaming console'])} from {vendor}."
        elif product_type == "luxury items":
            description = f"{character} indulged in luxury shopping at {vendor}."
        elif product_type == "rare artifacts":
            description = f"{character} acquired a rare artifact from {vendor}."
        elif product_type == "weapons":
            description = f"{character} bought a weapon from {vendor}."
        elif product_type == "web-slinging equipment":
            description = f"{character} restocked web-slinging equipment from {vendor}."
        elif product_type == "photography supplies":
            description = f"{character} purchased photography supplies from {vendor}."
        elif product_type == "dining":
            description = f"{character} enjoyed a meal at {random.choice(marvel_characters[character]['preferences'][product_type])}."

        # Randomize transaction amount
        if current_date.month == 3 and product_type == "electronics":
            amount = round(random.uniform(500, 2000), 2)  # Amplify electronics purchases in March
        else:
            amount = round(random.uniform(10, 200), 2)

        # Append transaction to the list
        transaction_id = len(transactions) + 1
        transaction = [transaction_id, current_date.strftime("%Y-%m-%d"), timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                       amount, product_type, character, vendor, description, location]
        transactions.append(transaction)

        # Move to the next day
        current_date += timedelta(days=1)

    return transactions

# Generate synthetic dataset
transactions_data = generate_synthetic_dataset()

# Write data to CSV file
with open('1IntroductionAndSetUp/3DataGeneration/transactionsEx0.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write headers
    writer.writerow(['Transaction ID', 'Date', 'Timestamp', 'Amount', 'Product Type', 'Character', 'Vendor',
                     'Transaction Description', 'Location'])
    # Write data rows
    writer.writerows(transactions_data)
