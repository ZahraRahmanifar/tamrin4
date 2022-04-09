from tkinter import N


a=input(('enter string plz'))
s='q0'
for i in range(len(N)):
    if s=='q0' and a[i]=='a':
        s='q1'  
if s=='q0':
    print('accept')
else:
    print('reject')
