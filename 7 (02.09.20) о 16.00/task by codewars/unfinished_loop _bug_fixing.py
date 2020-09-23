def create_array(n):
    res=[]
    i=1
    while i <= n: 
        res += [i]
        # res.append(i)
        i += 1
    return res

print(create_array(3))

# #########################

# def create_array(n):
#     return [i for i in range(1,n+1)]

# ########################

# create_array = lambda n: list(range(1,n+1))
