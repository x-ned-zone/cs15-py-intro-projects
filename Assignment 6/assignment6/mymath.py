 #calculate number of k-permutations of n items 
 #masixole ntshinga
 #17 april 2012 

def get_integer(t):
  n = input ("Enter "+t+":\n")
  while not n.isdigit ():
    n = input ("Enter "+t+":\n")
  n3 = eval (n) 
  return (n3)

def calc_factorial(n):
  nfactorial = 1
  
  for i in range (1, n+1):
    nfactorial *= i
    
  return nfactorial
