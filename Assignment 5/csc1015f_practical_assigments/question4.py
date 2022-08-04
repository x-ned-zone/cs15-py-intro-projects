from __future__ import print_function
import math
fx=input('Enter a function f(x):\n')

for y in range(20,-21,-1):
     for x in range(-20,+21):
          if y==round((eval((fx)))):
               print('*', end="")
          elif x==0 and y==0:
               print('+',end="")
          elif x==0 :
               print('|',end="")
          elif y==0:
               print('-',end="")
          else : 
               print(" ",end="")
     print()
