in_str = input("Enter a string:")
a=’’
d=0
r=1

for c in ’abcdefghijklmnopqrstuvwxyz’:
    if c in in_str:
        a = c + a
    else:
        d = d + 1
r += 2
print(a) # Line 1
print(d) # Line 2
print(r) # Line 3
