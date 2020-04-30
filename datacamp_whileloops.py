x = 1
while x < 4 :
    print(x)
    x = x + 1

# Basic while loop

offset = 8

while offset != 0:
    print('correcting...')
    offset = offset - 1
    print(offset)

# Add conditionals
# Initialize offset
offset = -6

while offset != 0:
    print("correcting...")
    if offset > 0:
      offset = offset - 1
    else: 
      offset = offset + 1  
    print(offset)
