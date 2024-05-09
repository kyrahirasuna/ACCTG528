
import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

def generate_data():
    # Initialize Faker and set random seed for reproducibility
    fake = Faker()
    Faker.seed(0)
    random.seed(0)

    # Define the date range
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 3, 31)

    # Helper function to generate random datetime within a range
    def random_datetime(start, end):
        """Generate a random datetime between `start` and `end`."""
        return start + timedelta(
            seconds=random.randint(0, int((end - start).total_seconds())),
        )

    # Define characters, products, vendors, and locations
    characters = ["Tony Stark", "Thor", "Peter Parker", "Bruce Banner", "Natasha Romanoff"]
    products = {
        "Tony Stark": ["Arc Reactor", "Iron Man Suit", "JARVIS AI"],
        "Thor": ["Mjolnir Replica", "Asgardian Armor", "Asgardian Ale"],
        "Peter Parker": ["Web Fluid", "Spider Suit", "Daily Bugle Subscription"],
        "Bruce Banner": ["Gamma Radiation Detector", "Stretchable Clothes", "Calm Tea"],
        "Natasha Romanoff": ["Black Widow Gear", "Espionage Tools", "Tactical Clothing"]
    }
    vendors = {
        "Arc Reactor": "Stark Industries",
        "Iron Man Suit": "Stark Industries",
        "JARVIS AI": "Stark Industries",
        "Mjolnir Replica": "Asgardian Antiques",
        "Asgardian Armor": "Asgardian Antiques",
        "Asgardian Ale": "Asgardian Antiques",
        "Web Fluid": "Parker Industries",
        "Spider Suit": "Parker Industries",
        "Daily Bugle Subscription": "Daily Bugle",
        "Gamma Radiation Detector": "Banner Tech",
        "Stretchable Clothes": "Banner Tech",
        "Calm Tea": "Banner Tech",
        "Black Widow Gear": "Red Room Inc",
        "Espionage Tools": "Red Room Inc",
        "Tactical Clothing": "Red Room Inc"
    }
    locations = {
        "Tony Stark": "Malibu, California",
        "Thor": "Asgard",
        "Peter Parker": "Queens, New York",
        "Bruce Banner": "Dayton, Ohio",
        "Natasha Romanoff": "St. Petersburg, Russia"
    }

    # Generating the transactions
    transactions = []
    for _ in range(10000):
        character = random.choice(characters)
        product = random.choice(products[character])
        vendor = vendors[product]
        location = locations[character]
        date = random_datetime(start_date, end_date)
        amount = round(random.uniform(5, 500), 2)  # Transaction amount between $5 and $500
        transaction_id = fake.uuid4()  # Unique transaction ID
        customer_id = fake.uuid4()  # Unique customer ID
        description = f"Purchase of {product} from {vendor}"

        transactions.append({
            "Transaction ID": transaction_id,
            "Date": date.date(),
            "Timestamp": date.strftime('%Y-%m-%d %H:%M:%S'),
            "Amount": amount,
            "Product ID": product,
            "Customer ID": customer_id,
            "Vendor": vendor,
            "Description": description,
            "Location": location
        })

    # Create DataFrame
    df_transactions = pd.DataFrame(transactions)

    # Save to CSV
    df_transactions.to_csv("Marvel_Universe_Transactions.csv", index=False)
    print("Dataset generated and saved to 'Marvel_Universe_Transactions.csv'.")

if __name__ == "__main__":
    generate_data()
