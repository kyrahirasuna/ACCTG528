The goal of this exercise is to prompt Chat GPT with instructions to make a realistic looking set of transactions. In this case we will ask for credit card information. In this folder is an example python code and csv output generated with the following prompt (note that this prompt was a little loose on the "realistic" part of the exercise instructions...):

I need assistance in developing a Python script to generate a synthetic dataset of 10,000 business transactions from January 1, 2024, to March 31, 2024. The dataset should include fields for transaction ID, date, timestamp, amount, product ID, customer ID (based on Marvel movie characters), vendor (using fictional settings inspired by the Marvel Universe), transaction description, and geographical information matching the character's associated fictional locations. Detailed requirements include:

Fictional Vendor Categorization: Transactions should be categorized under fictional outlets that would fit within the Marvel Universe, such as Stark Industries for high-end electronics, Asgardian Antiques for rare artifacts, or Daily Bugle Subscriptions for news.
Character and Product Alignment: Develop a detailed mapping of Marvel characters to product types and fictional vendors that aligns with their personas and typical expenditures, ensuring transaction descriptions span various activities like groceries, dining out, entertainment, etc.
Amounts and Descriptions: Set transaction amounts as random floats with two decimal places, reflecting the costs of items characters would plausibly purchase, with diverse descriptions depicting various types of activities.
Date and Time Distribution: Ensure dates and times are distributed randomly, with timestamps more frequent during daytime and in-store purchases limited to 10 AM to 9 PM.
Increased Electronics Purchases in March: Amplify electronics purchases in March, indicative of seasonal trends.
Geographical Data: Use specific fictional locations tied to each Marvel character to enhance the dataset's authenticity and relevance.
Output Format: Ensure the dataset is well-organized in a CSV file with proper headers and formatting for ease of use.
Detailed Specifications:

Data Consistency Checks: Implement checks to confirm that transaction amounts, descriptions, and fictional vendor types are consistent and logically align with the character-product-vendor mapping.
Dynamic Description Logic: Design logic to dynamically generate transaction descriptions based on the character’s likely activities and purchases, reflecting both the product type and the fictional vendor.
Peak Hours Emphasis: Develop a method for generating transaction timestamps more frequently during typical shopping peak hours to mimic real customer behavior patterns.
Character-Specific Geographical Metadata: Integrate fictional geographical metadata that corresponds to each Marvel character, enhancing the dataset's realism. Output all of this in a single code block