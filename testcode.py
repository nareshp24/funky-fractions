from FractionClass import *

#create a Fraction
print('creating a fraction f = 2/5')
f = Fraction(2, 5)
print('f = ', f)

#create another fraction in non-reduced form
print('creating a fraction g = 2/4')
g = Fraction(2, 4)
print('g = ', g)

#create a fraction in reduced form
print('creating a fraction h = 2/4 in reduced form by setting the "reduced" argument')
h = Fraction(2, 4, reduced = True)
print('h = ', h)

print()

#performing arithmetic operations on f and g
print('performing arithmetic operations on f and g')
print('f + g = ', f + g)
print('f - g = ', f - g)
print('f * g = ', f * g)
print('f / g = ', f / g)

print()

#performing comparison
print('performing comparison with f, g and h')
print('f < g: ', f < g)
print('f > g: ', f > g)
print('f <= g: ', f <= g)
print('f >= g: ', f >= g)
print('f == g: ', f == g)
print('f != g: ', f != g)
print('h == g: ', h == g)

print()

#check if f is a proper fraction
print('f = ', f, " is a proper fraction: ", f.is_proper())
#check if j = 5/2 improper fraction
j = Fraction(5, 2)
print('j = ', j, " is an improper fraction: ", j.is_improper())

print()

#testing get_numerator, get_denominator and get_reciprocal methods
print('numerator of f: ', f.get_numerator())
print('denominator of f: ', f.get_denominator())
print('reciprocal of f: ', f.get_reciprocal())

print()
#testing simplify method
k = Fraction(4, 6)
print('k = ', k, 'reduced form of k = ', k.simplify())
print('decimal equivalent of (f - g) = ', (f - g).to_decimal())

print()

#creating a fraction from string in
print("creating fraction from string input m = Fraction.from_string(6/8)")
print('m = ', Fraction.from_string('6/8'))

print()

#get multiples method
print('printing 1st 10 multiples of f = ', f)
n = f.get_multiples(10)
print(n)

print()

print('printing the multiples of f = ', f, 'from 5th to 10th multiple')
p = f.get_multiples(start = 5, stop = 10)
print(p)

print()
print('Hurray! Everything works just fine')











