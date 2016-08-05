
print "A circle/sphere calculator:"

radius = raw_input("radius of a circle(cm) = ")
x = radius
circumference = float(x)*2*3.14159
area = float(x)*float(x)*3.14159
volume = (float(x)*float(x)*float(x)*4*3.14159)/3
print 'circumference of the circle =',circumference,'cm'
print 'area of the circle =', area,'sq.cm'
print 'volume of the sphere =', volume, 'cubic cm'
print 'Would you like to use an english unit? '
ans = raw_input('answer (y or n) = ')
if ans == 'y':  #inch calculation
    y = radius
    circumference = float(x)*2*3.14159/2.54
    area = float(y)*float(y)*3.14159/((2.54)**2)
    volume = float(y)*float(y)*float(y)*4*3.14159/(3*((2.54)**3))
    print 'circumference of the circle =',circumference,'in.'
    print 'area of the circle =', area,'sq.in.'
    print 'volume of the sphere =', volume, 'cubic in.'
if ans == 'n':
    exit(0)
