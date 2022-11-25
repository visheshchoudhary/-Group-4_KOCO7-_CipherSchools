"""PROJECT NUMBER 4-----PASSWORD"""

import random
p=int(input("Length of password:- "))
x='abcdefghijklmnopqrstuvwxyz'
y='01234567890'
z='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s='!@#$%^&*()?'
a=(x+y+z+s)
m=""
for i in range(p):
 m=m+random.choice(a)
print(m)
def password_check(passwd):
    SpecialSym = s
    if len(passwd) < 12:
         print('Ignore that password')
    elif not any( (char.isdigit() for char in m) and (char.isupper() for char in m) and ((char.islower() for char in m))and ((char in SpecialSym for char in m))):
        print('Ignore that password')
    else:
        print('Good in streanth')
password_check(m)
  