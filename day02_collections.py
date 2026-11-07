from Data.sample_records import records

print("========== MINDMATE RECORD MANAGER ==========")

# Display all records
print("\n1. ALL RECORDS")

for record in records:
    print(record)


# Search records using a keyword
print("\n2. SEARCH RECORDS")

keyword = input("Enter keyword to search: ").lower()

found = False

for record in records:

    task = record["task"].lower()
    name = record["name"].lower()
    category = record["category"].lower()
    status = record["status"].lower()

    if (keyword in task or
        keyword in name or
        keyword in category or
        keyword in status):

        print(record)
        found = True

if not found:
    print("No matching records found.")


# Count records by category
print("\n3. COUNT RECORDS BY CATEGORY")

category_count = {}

for record in records:

    category = record["category"]

    if category in category_count:
        category_count[category] += 1

    else:
        category_count[category] = 1

for category, count in category_count.items():
    print(f"{category}: {count}")


print("\nTotal Records:", len(records))