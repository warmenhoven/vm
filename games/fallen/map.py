# map.py - Write map layout and room layout bytes to file
import os

# The map data
# First digit: room layout
# Second digit: door layout
# map size: 256 bytes
# segment 0 from start of file
# 32 columns is here           v
data = """
694A00698A003982724A0049328A006F
38854A38160083791A88723B1F73894B
007F837D253A7383230019823613781A
0053789A0013432775227B4F83231D86
5D813A3842811B288A008F587B43397B
002323000078123A187A2872428B7300
795B17322A0000230087321242725B00
83896B594534120132760049429A0000
73533926004E00330087321B00882A00
338746182A0059157A4300498C00789A
887B679C13007300132300887A492A33
00498B7F382C830023784A0023438313
8971148B0000488A53002300183B7826
4387258A00495C734300187484541246
837E0078943B499B3E1F003E23987C33
783C001D4B003872827B00004812826B
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
9B9100000000000000009091
A3A40000000000000000A3A4
A5A60000000000000000A5A6
919000000090910000009190
0000000000A3A40000000000
0000000000A5A60000000000
909100000091900000009B91
A3A40000000000000000A3A4
A5A60000000000000000A5A6
919000000000000000009190
FFE04900FFE04900
"""

# segment 4

data = data + """
000000000000000000000000
000000000000000000000000
000000000000000000000000
00000000A7A8A9AA00000000
00000000ABACADAE00000000
00000000AFB0B1B200000000
00000000B3B4B5B600000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
FFE04900FFE04900
"""

# Generic storage room
data = data + """
009D0000000000000000B700
009DB7000000000000009D00
00009D0000000000009D0000
000000000000000000000000
000000000000000000000000
000000000000000000000000
00000000000000000000009D
0000000000000000009D009D
009D000000000000009D9D9D
9D9DB700000000000000009D
FFE04900FFE04900
"""

# segment 5
# generic storage room
data = data + """
9D0000000000000000009B90
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000B7B79D000000000000
000000009D00000000000000
000000000000000000000000
000000000000000000000000
000000000000000000009091
000000000000000000009100
FFE04900FFE04900
"""

data = data + """
B80000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000B90000
000000000000000000000000
000000B90000000000000000
0000B8000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000009091
49FF4900FFE04900
"""

# segment 6

data = data + """
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
0000000000000000
"""

data = data + """
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
0000000000000000
"""

# segment 7

data = data + """
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
0000000000000000
"""

data = data + """
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
0000000000000000
"""

# segment 8

data = data + """
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
0000000000000000
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
