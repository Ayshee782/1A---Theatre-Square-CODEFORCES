import math

# Input: n = length, m = width, a = side of one tile
n, m, a = map(int, input().split())

# Calculate the number of tiles needed in each direction
tiles_length = math.ceil(n / a)
tiles_width = math.ceil(m / a)

# Total number of tiles
total_tiles = tiles_length * tiles_width

print(total_tiles)
