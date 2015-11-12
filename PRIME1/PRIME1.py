from math import sqrt
primes=[2]
output = ""
for i in range (3, 32000,2):
    isprime = True
    cap = sqrt(i)+1
    for j in primes:
        if j>cap:
            break
        if i%j==0 :
            isprime = False
            break
    if isprime:
        primes.append(i)




T = input()

for t in range(T):
    if t<>0 :
        output += "\n"
    
    m, n = raw_input().split()
    m, n = int(m), int(n)
    
    
    if m<=2 :
        islessthan2 = True
        if n>2:
            print 2
            m=3

        
    else:
        islessthan2 =False
        if m%2 == 0:
            m=m+1
    
    for i in range (m, n):
        if m==1 and n==2:
            break
        isprime = True
        cap = sqrt(i)+1
        for j in primes:
            if j>cap:
                break
            
            if i%j==0 :
                isprime = False
                if i==j:
                    isprime =  True
                break
            
        if isprime:
            output += "\n"+str(i)  


print(output)
#print f_primes
#print primes
