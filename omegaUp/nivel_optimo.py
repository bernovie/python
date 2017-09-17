a, b = map(int, raw_input().split())
if a > b:
    print "2", a - b
elif b > a:
    print "1", b - a
else:
    print "Nivel Optimo"
