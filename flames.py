name1=input("enter the first name").lower()
name2=input("enter the second name").lower()
name1=name1.replace(" ","")
name2=name2.replace(" ","")
for i in name1:
    for j in name2:
        if i==j:
            name1=name1.replace(i,"")
            name2=name2.replace(j,"")
            break
count=len(name1+name2)

if count>0:
    list1=["friends","lovers","affectionate","marriage","enemies","siblings"]
    while len(list1)>1:
        c=count%len(list1)
        s_index=c-1
        if s_index>=0:
            left=list1[:s_index]
            right=list1[s_index+1:]
            list1=right+left
        else:
            list1=list1[:len(list1)-1]
    print("relationship is ",list1[0])