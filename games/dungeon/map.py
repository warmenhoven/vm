# map.py - Write map layout and room layout bytes to file
import os

# The map data
# First digit: room layout
# Second digit: door layout
# map size: 256 bytes
# segment 0 from start of file
# 32 columns is here           v
data = """
090A00090A000902020A0009020A000E
08050A08060003090A08020B0E03090B
000F030D050A0303030009020603080A
0003080A0003030705020B0F03030D06
0D010A0802011B280A000F080B03090B
000303000008123A080A0802020B0300
090B07022A0000230007020202020B00
03090B094534120132060009020A0000
03030906000E00330007020B00080000
030706080A0009050A0300090C00080A
080B070C03000300030300080A090A03
00090B0F080C030003080A0003030303
0901040B0000080A03000300080B0806
0307050A00090C030300080404040206
030E0008040B090B0E0F000E03080C03
080C000D0B000802020B00000802020B
"""

# 10x12 room layouts
# room layout size: 128 bytes
# 10x12 = 120 bytes plus 8 bytes at the end for 4 colors for walls and 4 colors for tiles
# formula for letter/character:
# 
# x: index in alphabet of letter 0 - 25
# y: segment of memory
# z: offset in segment
# 
# y = floor(x / 16)
# z = x mod 16
# 
# for encoding in map.py as hexadecimal digits
# first digit = y + 1 
# because first digit 0 indicates an empty tile
# second digit = z
def encodeStringAsSprites(text):
    encoded = ""
    text = text.lower()
    for c in text:
        x = (ord(c) - ord('a'))
        y = x // 16
        z = x % 16
        encoded = encoded + format(y + 1, '1x') + format(z, '1x')
    return encoded

print(encodeStringAsSprites("fallen"))
print(encodeStringAsSprites("colony"))
# tile is empty if tile type is 0
# segment 1
# this is layout 0
# 24 columns is here   v
data = data + """
000000000000000000000000
009091000000000000909100
000000000000000000000000
009091000000000000909100
00000000002F300000000000
000000000031320000000000
000000960000000096000000
009200000000000000009300
009394000000000000949500
000000000000000000000000
FFE04900FFE04900
"""
#^ colors are 128, 96, 128 for walls and 255, 00, 00 for tiles

data = data + """
960000000000000000000096
000000000000000000000000
00002E000000009091000000
00000000000000999A000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000909500000000000000
000000979800000000000000
960000000000000000000096
FFE04900FFE04900
"""

# segment 2

data = data + """
91919B0000000000009B9191
910000000000000000000091
9B000000000000000000009B
000000000000000000000000
0000009100999A0000000000
000000909090909100000000
00000091999A000000000000
0000000000002E0000969600
969600000000000000000000
000000000000000000000000
FFE04900FFE04900
"""

data = data + """
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
00000000919C900000000000
000000000000000000000000
000000000000000000000000
9D000000000000000000009D
9D9D0000000000000000009D
FFE04900FFE04900
"""

# segment 3

data = data + """
9E9FA0A100000000A19E9EA0
000000000000000000000000
9EA1A09F00000000A29F9E9F
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
A2A09F9E00000000A19E9EA0
000000000000000000000000
A29F9E9F000000009EA1A09F
49FF4900FFE04900
"""

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

# segment 4

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

# segment 5

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

# segment 6

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

# segment 7

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

# segment 8

data = data + """
000000000000000000000000
011011000000000000121300
012000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
8060C000FF000000
"""
# This one is the title screen.
# It says:
#     FALLEN
#     COLONY
#
# Press Any Button

data = data + """
000000000000000000000000
0000000015101b1b141d0000
00000000121e1b1e1d280000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
00000000002A2B2C2D000000
000000000000000000000000
8060C000FF000000
"""

# segment 9

# Remove the newlines
data = data.translate(None, '\n')

# Convert from string to binary data
bin_data = data.decode("hex")

# Remove old file if it exists
if os.path.exists('mapdata'):
    os.remove('mapdata')

# Open the file in 'write binary' mode
out = open('mapdata', 'wb')

# Write to the file
i = 0
while i < len(bin_data):
    byte = bin_data[i]
    out.write(byte)
    i += 1

# Close the file
out.close()
