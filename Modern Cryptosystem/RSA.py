#picking two prime numbers
p= int(input("Enter the value of p: "))
q= int(input("Enter the value of q: "))
N = p*q

def phi(N):
    phi = (p-1)*(q-1)
    return phi

#choose number for e
# 1 < e < phi(N)
# e, N and phi(N) are coprime
import random
def gcd(a,b):
  while b!=0:
    a,b = b,a%b
  return a

def e(N):
    e = []
    for i in range(2,phi(N)):
        if gcd(i,N)==1 and gcd(i,phi(N))==1:
            e.append(i)
    ans = random.choice(e)
    return ans
print("Public Key: ",e(N)," ",N)
Lock = [e(phi(N)),N]
print(f"Lock: {Lock:{5}}")

#choose number for d
# 1 < d < phi(N)
# d and phi(N) are coprime
# d*e = 1 (mod (phi(N)))

def d(e,N):
  d = []
  for i in range(2, N):
    if (i*e)%phi(N) == 1 and gcd(i,phi(N))==1 and gcd(i,e)==1:
      d.append(i)
  ans = random.choice(d)
  return ans

key = [d(Lock[0],Lock[1]),N]
print(f"Key: {key:{5}}")