def numberx(n):
    ones=["","one","two","three","four","five","six","seven","eight","nine"]
    teens=["ten","elevent","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens=["","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
    thousands=["","thousand"]
    if n==0:
        return "zero"
    words=""
    if n>=1000:
        words+=ones[n//1000]+thousands[1]
        n%=1000
        if n>0:
            words+="and"
    if n>=100:
        words+=ones[n//100]+"hundred"
        n%=100
        if n>0:
            words+="and"
    if n>=20:
        words+=tens[n//10]
        n%=10
        if n>0:
            words+=ones[n]
    elif n>=10:
        words+=teens[n-10]
        n=0
    elif n>0:
        words+=ones[n]
    return words
def countw(n):
    t=0
    for i in range(1,n+1):
        word=numberx(n)
        word=word.replace(" ","").replace("-","")
        t+=len( word)
    return t
t=countw(1000)
print("Total letters are:",t)
