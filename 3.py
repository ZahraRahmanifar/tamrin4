a=input(('enter string plz'))

def DFA(strg):
    s='q0'
    for i in range(len(strg)):
        if s=='q0':
            s='q1'
        elif s=='q1':
            s='q2'
        elif s=='q2':
            s='q0'
    if s=='q0':
        return 'accept'
    else:
        return 'reject'
print(DFA(a))
    
