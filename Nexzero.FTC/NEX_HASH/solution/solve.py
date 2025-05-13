def hash(hi, x):
    
    out_arr = hi.copy()

    
    for xi in x:
        in_arr = out_arr.copy()
        
        # Apply 10 rounds
        for r in range(10):
            # Update the bytes
            A,B,C,D,E,F,G,H = out_arr
            out_arr[0] = (B + C + r) % 256 #A
            out_arr[1] = (A ^ C) % 256 #B
            out_arr[2] = (((C ^ xi)% 256) << 1) % 256 # C
            out_arr[3] = (C ^((F + r)% 256)) % 256 # D
            out_arr[4] = (G + ((E << 2)% 256)) % 256 # E
            out_arr[5] = G % 256 # F
            out_arr[6] = (G + ((xi << 2)% 256)) % 256 # G
            out_arr[7] = (G ^ ((H + r)% 256)) % 256 # H
            
            # Copy the output array back to the input array for the next round
            in_arr = out_arr.copy()

    # Return the final 8-byte hash as a hex string
    return ''.join(["{0:02x}".format(i) for i in out_arr])

def main():
    
    with open("/usr/share/wordlists/rockyou.txt", 'r', encoding='latin-1') as f:
        # Initial seed
        initial_seed = [ord('N'), ord('E'), ord('X'), ord('_'), ord('H'), ord('A'), ord('S'), ord('H')]  # 8-byte seed

        # Loop through each line in the wordlist
        for line in f:
            input_data = line.strip()  # Remove any extra whitespace or newlines

            # Convert input to byte values
            input_bytes = [ord(c) for c in input_data]

            # Generate the hash for the current word
            hash_value = hash(initial_seed, input_bytes)

            # Check if it matches the target hash
            if hash_value == 'f903467a43c75b9f':
                print(f"Matching word found! Word: '{input_data}', Hash: {hash_value}")
                break  # Stop once the matching hash is found

if __name__ == "__main__":
    main()
