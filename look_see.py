def look_say(number):
    res=''
    rep=number[0]
    number=number[1:]+' '
    times=1
    for actual in number:
        if actual!=rep:
            res+=str(times)+rep
            times=1
            rep=actual
        else:
            times+=1
    return res
num='1'
n=int(input())
for i in range(n):
    print(num)
    num=look_say(num)
