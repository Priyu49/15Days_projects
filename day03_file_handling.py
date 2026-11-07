# Writing data into a file

with open("mindmate.txt", "w") as file:
    file.write("Welcome to MindMate!\n")
    file.write("Your Personal Productivity Assistant.")

print("File created successfully!")

# Reading data from the file

with open("mindmate.txt", "r") as file:
    content = file.read()

print("\nFile Content:")
print(content)
