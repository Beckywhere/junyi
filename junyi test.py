#junyi test #gogogo

#1a將字串顛倒輸出
s = input()

print(s[::-1])


#B 單字本身反轉

s = input()
s1 = s.split()
for i in range(len(s1)):
    print(s1[i][::-1],end=" ")
    

#2

number1 = eval(input())
count = 0
for i in range(1,number1+1):
    if i%3==0 or i%5==0:
        if i%3==0 and i%5==0:
            count += 1
        else:
            continue
    else:
        count += 1
print(count)
        
