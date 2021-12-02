# Advent of code 2021 Dya 1

# To open the file
with open("./data/input_day1.txt") as f:
    depths = []

    # For every line in the file
    for line in f:
        # Add the INTEGER to a list of depths
        depths.append(int(line))

print(depths)
