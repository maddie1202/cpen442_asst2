f = open("input.txt", "r")
input = f.read()

mappings = {
    'A': 'm', #
    'B': 't', 
    'C': 'C',
    'D': 'n',
    'E': 'h',
    'F': 's',
    'G': 'a',
    'H': 'u',
    'I': 'I',
    'J': 'w',
    'K': 'r',
    'L': 'k',
    'M': 'd',
    'N': 'o',
    'O': 'j',
    'P': 'e',
    'Q': 'i',
    'R': 'l',
    'S': 'y',
    'T': 'g',
    'U': 'c',
    'V': 'f',
    'W': 'z',
    'X': 'p',
    'Y': 'v',
    'Z': 'b'
}

output = ''
for c in input:
    output += mappings[c]
print(output)
