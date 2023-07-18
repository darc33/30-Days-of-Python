def alphabet_position(text):
    text= text.lower()
    n =' '.join([str(ord(x)-96) for x in text if x.isalpha()]) 
    return print(n)

#alphabet_position("The sunset sets at twelve o' clock.")
alphabet_position('-46 -45 -46 -42 -41 -41 -42 -41 -43 -43')

def tribonacci(signature, n):
    if n==0:
        return []
    elif n<=3:
        return signature[:n]
    else:
        for i in range(n-3):
            signature.append(sum(signature[-3:]))
        return signature

print(tribonacci([1, 1, 1], 10))