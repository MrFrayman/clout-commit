# app.py should read the contents of data.txt and just replace it with a random char from [a-z] (excluding the one currently in data.txt). This way you don't get arbituary big files...

import random
import string

def main():
    with open('data.txt', 'r') as f:
        current_char = f.read().strip()
    
    # Generate a random character from a-z excluding the current character
    possible_chars = [c for c in string.ascii_lowercase if c != current_char]
    new_char = random.choice(possible_chars)
    
    # Write the new character back to data.txt
    with open('data.txt', 'w') as f:
        f.write(new_char)

if __name__ == "__main__":
    main()
