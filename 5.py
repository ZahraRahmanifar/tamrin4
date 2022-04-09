a=input(('enter string :'))
s='q0'
for i in range(len(a)):
    if(a[i]=='a' and s=='q0'):
        s='q1'
    elif(a[i]=='b' and s=='q0'):
        s='q1'
    elif(a[i]=='a' and s=='q1'):
        s='q2'
    elif(a[i]=='b' and s=='q1'):
        s='q2'
    elif(a[i]=='a' or a[i]=='b' and s=='q2'):
        s='q1'
    
if(s=='q1'):
    print("accept")
else:
    print("reject")

