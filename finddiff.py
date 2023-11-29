s = 'codeforces'
h = list(s)
k = input("")
g = set(k)
if k == h:
    print(0)  
else:     
    for j in g:
        if j in h:
            h.remove(j)
    print(len(h))        
            
        

