# First non-repeating character
def non_rep_char(str1):
    list1=[]
    list1.extend(str1)
    feq={}
    for i in list1:
        if i in feq:
            feq[i]+=1
        else:
            feq[i]=1

    for i in list1:
        if feq[i]==1:
            return i
    

    return None

print(non_rep_char("aabbcc"))