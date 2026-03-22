import math

num=23.45
print("Ceil and floor value:", math.ceil(num), math.floor(num))

x=10
y=-15

resultsign=math.copysign(x,y)
print("The sign of the result is:", resultsign)

abs1=math.fabs(-96)
abs2=math.fabs(56)
print("Absolute values:", abs1, abs2)

gcdresult=math.gcd(48,18)
print("GCD of 48 and 18 is:", gcdresult)