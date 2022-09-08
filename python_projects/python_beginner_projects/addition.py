x = 'adbec'
y = 'bec'

j = len(x)
n = len(y)

z = x[slice(j-n,None,1)]
print(z)

if z == y:
    print ('it worked')

else:
    print('nope')