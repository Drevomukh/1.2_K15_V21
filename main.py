import math

x = -49

if ( x < 16 ):
    result = x ** 5 - 68 * x ** 7 + 46
elif ( 16 <= x < 109 ):
    result = math.log(math.e, math.cos(x) - 93 * x - 71) + x ** 5
elif ( 109 <= x <= 151 ):
    result = 88 * x ** 8 + x - 60
elif ( x >= 151 ):
    result = 19 * (math.fabs(x) + math.cos(x)) ** 4 - math.fabs(x)

print(f"{result:.2e}")
