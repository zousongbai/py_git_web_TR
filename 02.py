# @author       ：小青年
# @ProjectName  ：py_web_TR_boss
# @Name         ：02
# @time         ：2020/4/17 10:02 

# a=[1,2,3,4,5,6,7]
# b=[]
# for i in a:
#     if (i+1)%2==1:
#         b.append(6)
#     else:
#         b.append(i)
# print(b)


# a='1 3 a* d2'
# # b=a.split('*')
# # print(a.split())
# # c=''.join(b)
# # print(c)
# b=a.replace(' ','')
# print(b)
# # replace()方法，可以去除全部空格

# pwd1='1234'
#
# count=3
# while count>0:
#     user_pwd = input('请输入用户名密码：')
#     if user_pwd!=pwd1:
#         count-=1
#         print('密码出入错误，还剩{}次'.format(count))
#     else:
#         print('恭喜您！密码输入正确')

# import requests
# print(requests.get.__doc__)


li = [1,2,3,4,5,6,7,8,9]
li2=[x**2 for x in li]
print(li2)