# Taking inputs separately
n = int(input("Enter the length of the square (n): "))
m = int(input("Enter the width of the square (m): "))
a = int(input("Enter the side of the tile (a): "))

# Use ceiling logic without math.ceil()
tiles_length = (n + a - 1) // a
tiles_width = (m + a - 1) // a

# Total number of tiles
total_tiles = tiles_length * tiles_width

print("Minimum number of tiles needed:", total_tiles)
