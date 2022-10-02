from email import message
import sys

f = open(sys.argv[1],"r")
contents = f.readlines()
p, q = 0 , 0
list = []

def phi (p, q):
    phi = (p-1)*(q-1)
    return phi

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None    

def coprimes(a):
    list = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x,Et) != None:
            list.append(x)
    for x in list:
        if x == modinv(x,Et):
            list.remove(x)
    return list

def encrypt(m):
    c = modinv(m**e, n)
    return c

def decrypt(c):
    m = modinv(c**d, n)
    return m


for i in contents:
    if " " in i:
        #read p and q values
        pstring, qstring = i.split()
        p = int(pstring)
        q = int(qstring)
        n = (p * q)

        #Calculate the Euler totient
        Et = phi(p, q)
        #Calculate a list of eligible coprimes of ɸ(n).
        options = coprimes(Et)

        e = options [2]

        d = modinv(e,Et)

        #public key (e,n) private key (d,n)

    else:
        #encrypt and decrypt input messages
        messageIn = int(i)
        cipher = encrypt(messageIn)
        decryptMessage = decrypt(cipher)

        #Output
        output = f"p: {p}, q: {q}, n: {n}, phi: {Et}, e: {e}, d: {d}, message: {messageIn}, encrypted: {cipher}, decrypted: {decryptMessage}"
        print(output)




