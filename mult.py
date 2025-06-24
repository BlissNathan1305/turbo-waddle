# Define the size of the multiplication table
size = 10

# Print the header row
print("   |", end="")
for i in range(1, size + 1):
    print(f"{i:4}", end="")
print()
print("---" + "----" * size)

# Print the multiplication table
for i in range(1, size + 1):
    print(f"{i:3} |", end="")
    for j in range(1, size + 1):
        print(f"{i * j:4}", end="")
    print()
