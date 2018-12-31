#check if input is integer
def is_int(input):
    '''returns true if the input is an integer'''
    try:
        _tempVar = int(input)
    except ValueError:
        return False
    return True

#greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a



class Fraction:

    #constructor
    def __init__(self, top = 0, bottom = 1, reduced = False):
        if not (is_int(top) and is_int(bottom)):
            raise ValueError("numerator and denominator must be valid literal of type 'int'")

        if (type(top) or type(bottom)) is float:
            raise ValueError("numerator and denominator must be valid literal of type 'int'")

        bottom = int(bottom)
        if bottom == 0:
            raise ZeroDivisionError("denominator should be a non-zero 'int'")

        #the variable self._common is the gcd of numerator and denominator which is calculated only if reduced == True
        self._common = 1
        if reduced:
            self._common = abs(gcd(top, bottom))
        
        if bottom < 0:
            self._num = -int(top)//self._common
            self._den = -bottom//self._common

        else:
            self._num = int(top)//self._common
            self._den = bottom//self._common

    #display method
    def show(self):
        '''displays the fraction'''
        
        print(self._num, "/", self._den)

    #overriding the default __str__
    def __str__(self):
        if self._den == 1:
            return str(self._num)
        return str(self._num) + "/" + str(self._den)

    #overriding the default __repr__
    def __repr__(self):
        return str(self)

    #Greatest common divisor as a method 
    def gcd(self):
    	'''
    		returns the Greatest Common Divisor of numerator and denominator of fraction.

    		Example
    		-------
    		>>>common = Fraction(5, 10).gcd()
    		>>>common
    		5
    	'''
    	
    	a = self._num
    	b = self._den

    	while b != 0:
    		a, b = b, a % b

    	return a
            
    #add (+) method
    def __add__(self, rhs):
        '''returns the sum of fractions in reduced form'''
        # (a/b) + (c/d) = (ad + bc)/bd

        if type(rhs) is int:
            rhs = Fraction(rhs, 1)

        newnum = (self._num * rhs._den) + (self._den * rhs._num)
        newden = self._den * rhs._den
        #common = Fraction(newnum, newden).gcd()

        #return Fraction(newnum//common, newden//common)
        return Fraction(newnum, newden, reduced = True)

    # equal (==) method
    def __eq__(self, rhs):
        '''returns true if the calling object is equal to the passed object'''

        if type(rhs) is int:
            rhs = Fraction(rhs, 1)

        firstnum = self._num * rhs._den
        secondnum = rhs._num * self._den

        return firstnum == secondnum

    #sub (-) method
    def __sub__(self, rhs):
        '''returns the difference of fractions in reduced form '''
        # (a/b) - (c/d) = (ad - bc)/bd

        if type(rhs) is int:
            rhs = Fraction(rhs, 1)
        
        newnum = (self._num * rhs._den) - (self._den * rhs._num)
        newden = self._den * rhs._den
            
        #common = Fraction(newnum, newden).gcd()

        #return Fraction(newnum//common, newden//common)
        return Fraction(newnum, newden, reduced = True)

    #multiply (*) method
    def __mul__(self, rhs):
        '''returns the product of fractions in reduced form'''

        if type(rhs) is int:
            rhs = Fraction(rhs, 1)

        newnum = self._num * rhs._num
        newden = self._den * rhs._den
        #common = Fraction(newnum, newden).gcd()
        
        #return Fraction(newnum//common, newden//common)
        return Fraction(newnum, newden, reduced = True)

    #divide (/) method
    def __truediv__(self, rhs):
        '''returns the quotient of the fractions in reduced form'''
        #(a/b) / (c/d) = (ad)/(bc)
        if type(rhs) is int:
            rhs = Fraction(rhs, 1)
        
        newnum = self._num * rhs._den
        newden = self._den * rhs._num
        #common = Fraction(newnum, newden).gcd()

        #return Fraction(newnum//common, newden//common)
        return Fraction(newnum, newden, reduced  = True)

    #less than( < ) method
    def __lt__(self, rhs):
        '''returns true if the calling object is smaller than passed object'''

        if type(rhs) is int:
            rhs = Fraction(rhs, 1)
        
        parProd_1 = self._num * rhs._den
        parProd_2 = self._den * rhs._num

        if parProd_1 < parProd_2:
            return True

        return False

    #greater than( > ) method
    def __gt__(self, rhs):
        '''returns true if the calling object is greater than passed object'''

        if type(rhs) is int:
            rhs = Fraction(rhs, 1)

        partialProduct_1 = self._num * rhs._den
        partialProduct_2 = self._den * rhs._num

        if partialProduct_1 > partialProduct_2:
            return True

        return False

    #not equals to ( != ) method
    def __ne__(self, rhs):
        '''returns true if the calling object and the passed object are not equal'''

        if type(rhs) is int:
            rhs = Fraction(rhs, 1)

        partialProduct_1 = self._num * rhs._den
        partialProduct_2 = self._den * rhs._num

        if partialProduct_1 != partialProduct_2:
            return True

        return False

    #less than or equal to( <= ) method
    def __le__(self, rhs):
        '''returns true if the calling object is smaller than or equal to the passed object'''

        if type(rhs) is int:
            rhs = Fraction(rhs, 1)

        partialProduct_1 = self._num * rhs._den
        partialProduct_2 = self._den * rhs._num

        if partialProduct_1 <= partialProduct_2:
            return True

        return False

    #greater than or equal to( >= ) method
    def __ge__(self, rhs):
        '''returns true if the calling object is greater than or equal to the passed object'''

        if type(rhs) is int:
            rhs = Fraction(rhs, 1)

        partialProduct_1 = self._num * rhs._den
        partialProduct_2 = self._den * rhs._num

        if partialProduct_1 >= partialProduct_2:
            return True

        return False

    #check if fraction is a proper fraction
    def is_proper(self):
        ''' returns true if the numerator greater than or equal to denom'''
        return self._num <= self._den

    #check if fraction is an improper fraction
    def is_improper(self):
        ''' returns true if the numerator greater than or equal to denom'''
        return self._num < self._den

    #get numerator of the fraction
    def get_numerator(self):
        '''returns the numerator of the fraction'''
        return self._num

    #get denominator of the fraction
    def get_denominator(self):
        '''returns the denominator of the fraction'''
        return self._den

    #get reciprocal or multiplicative inverse of the function
    def get_reciprocal(self):
        '''returns reciprocal or multiplicative inverse of the fraction'''
        return Fraction(self._den, self._num)

    #get the desired number of multiples of a fraction
    def get_multiples(self, stop, start = None):
        '''returns a list of integer multiples of the fraction'''

        if start == None:
            start = 1

        multiples_list = []
        for i in range(start, stop + 1):
            newnum = self._num * i
            #common = Fraction(newnum, self._den).gcd()
            #multiples_list.append(Fraction(newnum//common, self._den//common)
            multiples_list.append(Fraction(newnum, self._den, reduced = True))

        return multiples_list

    #reduce the fraction
    def simplify(self):
        '''returns the simplified ratio of the fraction'''
        #common = Fraction(self._num, self._den).gcd()

        #return Fraction(self._num//common, self._den//common)
        return Fraction(self._num, self._den, reduced = True)

    #convert the fraction to decimal
    def to_decimal(self):
        '''returns the decimal equivalent of the fraction'''
        return self._num / self._den

    #create a fraction from string
    def from_string(string):
        '''creates and reaturns a fraction from string input 'a/b' '''
        return Fraction(*[int(num) for num in string.split('/')])

    #destructor
    #def __del__(self):
     #   '''destructor method'''
      #  print("Object has been destroyed")


    
   

    

        
            


    
