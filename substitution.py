f = open("input.txt", "r")
input = f.read()

mappings = {
    'A': 'm', #
    'B': 'B', 
    'C': 'C',
    'D': 'n', #
    'E': 'h', ##
    'F': 't', ##
    'G': 'a', #
    'H': 'i',
    'I': 'I',
    'J': 't',
    'K': 'K',
    'L': 'L',
    'M': 'd', #
    'N': 'o', #
    'O': 'O',
    'P': 'e', ##
    'Q': 'Q',
    'R': 'R',
    'S': 'S',
    'T': 'T',
    'U': 'c', #
    'V': 'r',
    'W': 'W',
    'X': 'X',
    'Y': 'Y',
    'Z': 'Z'
}

output = ''
for c in input:
    output += mappings[c]
print(output)
