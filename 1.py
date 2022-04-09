a=input(('enter string plz'))

def DFA(strg):
    s='q0'
    for i in range(len(strg)):
        if s=='q0':
            s='q0'
    if s=='q0':
        return 'reject'
   
print(DFA(a))
