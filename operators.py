myNumber1 = 30
myNumber2 = 40

# Arithmetic operators [A/o]

# (+) = addition A/o - added two numbers
print(myNumber1 + myNumber2)

# (-) = subtraction A/o - Subtract two numbers
print(myNumber1 - myNumber2)

# (*) = multiply A/o - Multiply two numbers
print(myNumber1 * myNumber2)

# (/) = Division A/o - To divide two numbers
print(myNumber1 / myNumber2)

# (**) = Exponent A/o - to find the power
print(myNumber1 ** 2)
print(myNumber2 ** 4)

# (%) = Modulus/Remainder A/o - to find the remainder of a division
print(myNumber2 % myNumber1)

# (//) = Integer Division - Give the quotient of the division
print(myNumber2 // myNumber1)

# Comparison Operator or Relational Operator
"""
    > Greater Than
    >= Greater Than Equals to
    < Less than 
    <= Less than Equals to
    == Equals t0
    != Not Eqals to
    
"""

print(myNumber1 > myNumber2)
print(myNumber1 >= myNumber2)
print(myNumber1 < myNumber2)
print(myNumber1 <= myNumber2)
print(myNumber1 == myNumber2)
print(myNumber1 != myNumber2)

# Logical / Boolean Operator
"""
    and - Return true if both condition is true
    or - Return true if one condition is true
    not - If true return false if false return true

"""

print(myNumber1 > myNumber2 and myNumber1!=myNumber2)
print(myNumber1 > myNumber2 or myNumber1!=myNumber2)
print(not(myNumber1 > myNumber2 and myNumber1!=myNumber2))

# Membership Operator
"""
    in - return true if an element is found in certain sequence.
    not in - return true if an element is not found in certain sequence

"""
myList = ["Kanishk", "Ayansh", "Ayushi"]
print("Ayushi" in myList)
print("Kanishk" not in myList)
