import csv

records = [
    {
        "id": 1,
        "title": "Complete Python",
        "category": "Learning",
        "priority": "High",
        "status": "Pending"
    },
    {
        "id": 2,
        "title": "Build MindMate",
        "category": "Project",
        "priority": "High",
        "status": "In Progress"
    }
]

# Writing CSV
with open("tasks.csv", "w", newline="") as file:

    fieldnames = ["id", "title", "category", "priority", "status"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(records)

print("CSV file created successfully!")

# Reading CSV
with open("tasks.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)