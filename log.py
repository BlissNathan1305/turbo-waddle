import math

# Define the range of numbers
start = 1
end = 10

# Print the header row
print("Number | Logarithm (base 10) | Natural Logarithm")
print("------|--------------------|")

# Print the logarithmic table
for i in range(start, end + 1):
    log10 = round(math.log10(i), 4)
    ln = round(math.log(i), 4)
    print(f"{i:6} | {log10:18} | {ln}")
