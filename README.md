# RSA-Algorithm
Building the RSA (public/private-key) Encryption Algorithm in python

Run with the command `python rsa.py input.txt`

Input must be in the format: 
67 83
24
29
31
16
13
71 83
21
32
13
49
39

Sample Output: 
p: 67, q: 83, n: 5561, phi: 5412, e: 13, d: 1249, message: 24, encrypted: 3658, decrypted: 24
p: 67, q: 83, n: 5561, phi: 5412, e: 13, d: 1249, message: 29, encrypted: 1838, decrypted: 29
p: 67, q: 83, n: 5561, phi: 5412, e: 13, d: 1249, message: 31, encrypted: 87, decrypted: 31
p: 67, q: 83, n: 5561, phi: 5412, e: 13, d: 1249, message: 16, encrypted: 2600, decrypted: 16
p: 67, q: 83, n: 5561, phi: 5412, e: 13, d: 1249, message: 13, encrypted: 928, decrypted: 13
p: 71, q: 83, n: 5893, phi: 5740, e: 11, d: 3131, message: 21, encrypted: 1766, decrypted: 21
p: 71, q: 83, n: 5893, phi: 5740, e: 11, d: 3131, message: 32, encrypted: 4947, decrypted: 32
p: 71, q: 83, n: 5893, phi: 5740, e: 11, d: 3131, message: 13, encrypted: 3242, decrypted: 13
p: 71, q: 83, n: 5893, phi: 5740, e: 11, d: 3131, message: 49, encrypted: 4511, decrypted: 49
p: 71, q: 83, n: 5893, phi: 5740, e: 11, d: 3131, message: 39, encrypted: 2366, decrypted: 39