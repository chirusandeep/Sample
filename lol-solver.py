lol_file = open("lol", "r")
lol_contents = lol_file.read()

lol_in_binary = ""

for character in lol_contents:
    if ord(character) == 32:
        lol_in_binary += "0"
    if ord(character) == 9:
        lol_in_binary += "1"

decoded_string = ""

for index in range(0, len(lol_in_binary), 8):
    decoded_string += chr(int(lol_in_binary[index:index+8], 2))

print "Flag is: %s"%(decoded_string)
