#python3
def lastdigit(n):
        m = 10
        p = 60
        np = n % p
        if np == 0:
                return np
        else:
                f = []
                f.append(0)
                f.append(1)
                c = 1
                for i in range(1,np):
                    a = ((f[i] % 10) + (f[i-1] % 10)) % 10
                    c = (c + a) % 10
                    f.append(a)
                    #print(a)
                return c                 
    
    
        
        

n = int(input())
print(lastdigit(n))
        
    
    
    
        
    