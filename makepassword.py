import random
import string

smailar_chars = '0o1ilLIOpP'
upper = "".join(set(string.uppercase) - set(smailar_chars))
lower = "".join(set(string.lowercase) - set(smailar_chars))
symbols = '#$%&+,-./:;_~?=@!'
numbers = "".join(set(string.digits)-set(smailar_chars))
chars = upper+lower
groups = (chars, upper, lower, symbols)

def genpass(n, length):
    passwd = []
    k = 1
    while k <= n:
        pw = [random.choice(i) for i in groups]
        con = ''.join(groups)
        for i in range(length-len(pw)):
            pw.append(random.choice(con))
        random.shuffle(pw)
        passwd.append(''.join(pw))
        k += 1
    return passwd
def main():
    num = raw_input("pls input password num:")
    length = raw_input("pls input password bit:")
    print genpass(int(num), int(length))

if __name__ == '__main__':
    main()
