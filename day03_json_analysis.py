import json

with open("Data/raw/api_tasks.json", "r") as file:
    records = json.load(file)

completed = 0
pending = 0

for task in records:

    if task["completed"]:
        completed += 1
    else:
        pending += 1

print("Total Tasks:", len(records))
print("Completed Tasks:", completed)
print("Pending Tasks:", pending)

print("\nFirst 5 Tasks:")

for task in records[:5]:
    print(
        task["id"],
        task["title"],
        task["completed"]
    )
    