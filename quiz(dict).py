q1="""what is in the bracket [a]
a.a
b.ab
c.gh
d.fg """
q2="""what is in the bracket [b]
a.a
b.b
c.gh
d.fg """
q3="""what is in the bracket [c]
a.a
b.ab
c.c
d.fg """
questions={q1:"a",q2:"b",q3:"c"}
name=input("enter the name")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("do you want to skip this question (yes or no):")
    if flag1=="yes":
        continue
    ans=input("enter the answer a/b/c/d:")
    if ans==questions[i]:
        print("correct answer you got a point")
        score=score+1
        print("your current score",score)
    else:
        print("wrong answer you lose one point")
        score=score-1
        flag2=input("do u want quit (yes or no):")
        if flag2=="yes":
            break
print("ur final score is ",score)