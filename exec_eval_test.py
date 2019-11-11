#_*_coding:UTF-8_*_
#开发人员:Administrator
#开发时间:2019/10/22 10:54
import random
import logging
code='''
i=0
list1=[]
while i<10:
    list1.append(random.randint(0,100))
    i+=1
print(list1)    
'''
exec(code)
log = '{"a":1,"b":2}'
log1 = eval(log)
print(log1)