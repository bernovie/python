a = int(raw_input())
if a % 100 != 0:
    if a % 4 == 0:
        print "S"
    else:
        print "N"
else:
    if a % 400 == 0:
        print "S"
    else:
        print "N"
