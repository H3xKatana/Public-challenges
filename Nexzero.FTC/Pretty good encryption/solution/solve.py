import random
import time
from Crypto.Util.number import isPrime
from Crypto.Util.number import bytes_to_long, long_to_bytes

def generate_prime(bits, seed):
    random.seed(seed)
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1  
        if isPrime(num):
            return num

def generate_rsa_params(seed):
    p = generate_prime(512, seed)
    q = generate_prime(512, seed + 1)
    n = p * q
    e = 65537
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    return (n, e), (d, p, q),phi,d




# Create RSA key
def rsa_encrypt(message, public_key):
    n,e= public_key
    m = bytes_to_long(message)
    return pow(m, e, n)

def rsa_decrypt(cipher, priv):
    d,p,q=priv
    n=p*q
    m=pow(cipher,d,n)
    message = long_to_bytes(m)
    return message

def main():
    with open("flag.enc", "rb") as f:
        flag_enc = f.read()
    
    flag_enc=int(flag_enc)
    '''
    final timestamp solutino
    print(flag_enc)
    pub, priv, phi, d = generate_rsa_params(1735926966)
    message=rsa_decrypt(flag_enc, priv)
    print(message)
    '''
    # Start timestamp and range
    # look at timestamp.py to get the timestamp and understand how we got the time stamp
    start_timestamp = 1735926987
    
    # Iterate over a range of timestamps
    for timestamp in range(start_timestamp-1000, start_timestamp+1000 ):
        print("### log trying timestamp ",timestamp)
        print("### iteratino ",timestamp-start_timestamp)
        pub, priv, phi, d = generate_rsa_params(timestamp)
        
        try:
            # Attempt decryption
            message = rsa_decrypt(flag_enc, priv)
            
            # Check if the flag exists in the message
            if b'nexus' in message:
                print(f"Flag found! Timestamp: {timestamp}")
                print(message)
                break  # Stop searching after finding the flag
        except Exception as e:
            # Handle decryption errors gracefully
            pass




main()