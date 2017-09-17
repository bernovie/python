
limit = input("Enter number limit for prime: ")
for n in xrange(limit):
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
        if n != 2 and n != 3 and n != 5:
            print n,

