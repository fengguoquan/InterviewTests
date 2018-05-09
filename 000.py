#coding:utf-8#

# a = lambda n : 1 if n==1 else a(n-1)+n
# print a(4)

# a)=[]
# a.append([0,0])
# print(a[0])
# a[0]=1
# print(a


# a = [[]]
# a[0].append(2)
# a[1].append(2)
# a[2].append(2)
# print(a)


# for i in range(0, 10):
#   map += [[]]
#   for j in range(0, 20):
#     map[i] += ['*']
#
# print(map)


# map = [[1,2,3] for i in range(5)]
# print(map)
#
# map[0]=[1,1,1]
# print(map)

# a = lambda x,y : 1 if x==0 or y==0 else a(x-1,y)+a(x,y-1)
# print(a(2,2))
#
# import re
# a=re.compile(r'o{1,3}',re.S)
# print a.findall('foooooood')
import re
# line = "Cats are smarter than Cats dogs "
# matchObj = re.match( r'(?P<name>.*) are (.*?) (?P=name) (.*)', line, re.M|re.I)
# if matchObj:
#     print "matchObj.group() : ", matchObj.group()
#     print "matchObj.group(1) : ", matchObj.group(1)
#     print "matchObj.group(2) : ", matchObj.group(2)
#     print "matchObj.group(3) : ", matchObj.group(3)
#
#     print(matchObj.group('name'))
#
# else:
#     print "No match!!"
# line = '-000dgfhfgh-254bhku289fgdhdy675gfh'
# a= re.compile(r'(.*?\d+.*)+')
# b = a.match(line)
# print b.groups()
#

# a = raw_input('haha:')
# print(a)
# print(type(a))
# print -10%3




# a = [1,3,5,7,4,2,9]
#
# for i in range(len(a)-1):
#     for j in range(len(a)-i-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
#
# print(a)

# x = 2
# y = 3
#
# a = y-3 and x or y
# print(a)

# a = (x for x in range(10))
# print(a)

# class Person:
#     name = [2,3,4]
#
#
# p1 = Person()
# p2 = Person()
# p1.name = [3,4,5]
# print p1.name  # bbb
# print p2.name  # aaa
# print Person.name  # aaa

# line= 'asdf sldkjf  ee  2345  sldkjf'
# m=re.compile(r'\d+?')
# a= m.findall(line)
# print(a)

pattern = re.compile(r'hello')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match1 = pattern.match('hello world!')
match2 = pattern.match('helloo world!')
# match3 = pattern.match('helllo world!')
#
# # 如果match1匹配成功
# if match1:
#     # 使用Match获得分组信息
#     print match1.groups()
# else:
#     print 'match1匹配失败！'
#
# # 如果match2匹配成功
# if match2:
#     # 使用Match获得分组信息
#     print match2.group()
# else:
#     print 'match2匹配失败！'
#
# # 如果match3匹配成功
# if match3:
#     # 使用Match获得分组信息
#     print match3.group()
# else:
#     print 'match3匹配失败！'
# import re
# a = '.sdf..ddd'
# b = re.split(r'\.',a,3)
# print(b)

# a = [4,6,5,5,4,6,7]
# print(set(a))
# import copy
# a = [2555,'douyu',[4,5],'douyu']
# b = copy.copy(a)
# c = a
# print(a ,b ,c)
# print(id(a[2]))
# a.append(9)
# a[2][1]=9
# print(a,b,c)
# print(id(a[2]))
# # print(a[1] is b[4])
# # print(a[1] == b[4])
# print(id(a))
# print(id(b))
# print(a is b)
# print(a)
# print(b)
# a[0]=4444
# a[2]=[4,7]
# print(a)
# print(b)
# print(id(a[2]))
# print(id(b[2]))




# a = [{'x':1,'y':2},{'x':1,'y':5},{'x':1,'y':2},{'x':2,'y':4}]
#
# def haha(items,key=None):
#     seen = []
#     for item in items:
#         val  =  item if key is None else key(item)
#         print(seen)
#         print(val)
#
#         if val  not in seen:
#             yield item
#             seen.append(val)
#
# c = list(haha(a,key = lambda d : (d['x'],d['y'])))
# e = list(haha(a,key = lambda d : (d['x'])))
# print(c)
# print(e)

# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         # print b
#         a, b = b, a + b
#         n = n + 1
# print(list(fab(5)))



#
# funcs = [lambda  x: x+n for n in range(5)]
# print(funcs)
# for f in funcs:
#     print(f(0))





# a = []
# for i in range(2):
#     b = {'i':i}
#     a.append(b)
# print(a)

# a = []
# b = {}
# for i in range(2):
#     b ['i'] = i
#     print(b)
#     a.append(b)
#     print(a)
# print(a)
# print(id(a[0]))
# print(id(a[1]))


# a = []
# b = {'i':0}
# a.append(b)
# print(a)
# b['i']= 1
# a.append(b)
# print(a)

a = []
b = {}
for i in range(2):
    b[i] = i
    print(b)
    a.append(b)
    print(a)
print(a)

# a= [i+3 for i in range(4)]
# print(a)



























