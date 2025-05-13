from Cryptodome.Cipher import ARC4
import hashlib
import time
import sys

def decrypt_file(encrypted_file, output_file):
    # Known secret
    secret = "mambacoresecure"
    
    # Read encrypted data
    with open(encrypted_file, 'rb') as f:
        encrypted_data = f.read()
    
    # Try timestamps in a range around the given time
    time_range = 10000 # Search 60 seconds before and after
    base_timestamp = 1745061386
    
    print(f"Starting brute force around timestamp {base_timestamp}")
    
    for i in range(time_range):

        test_time = base_timestamp -  i
        print(f"Trying timestamp: {test_time}")
        # Generate key using the same method as encryption
        
        test_key = hashlib.md5(f"{test_time}{secret}".encode()).digest()
        
        # Create cipher and attempt decryption
        cipher = ARC4.new(test_key)
        decrypted_data = cipher.decrypt(encrypted_data)

        # Check if the decrypted data contains the expected plaintext
        
        if decrypted_data.startswith(b'PK\x03\x04'):
            print(f"\nFound valid ZIP signature at timestamp {test_time}")
            
            # Save the decrypted ZIP file
            with open(output_file, 'wb') as f:
                f.write(decrypted_data)
            print(f"Successfully decrypted and saved to {output_file}")
            return True
            
    print("\nFailed to find correct timestamp - No valid ZIP file found")
    return False
        
        
        
    
    print("\nFailed to find correct timestamp")
    return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python brute_force_decrypt.py <encrypted_file> <approximate_timestamp> <output_file>")
        sys.exit(1)
    #19:27:01
    encrypted_file = sys.argv[1]
    
    output_file = sys.argv[2]
    
    decrypt_file(encrypted_file, output_file)