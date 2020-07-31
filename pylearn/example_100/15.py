# -*- coding: utf-8 -*-

score=int(input("请输入你的成绩:"))
if score>=90:
    grade='A'
elif score>=60:
    grade='B'
else:
    grade='C'
print('你的成绩:'+str(grade))