# -*- coding: utf-8 -*-
'''
list  可以随时添加和删除其中的元素
classmates = ['Michael', 'Bob', 'Tracy']

tuple  一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')

dict  一定要有key值 初始化或通过key放入
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

set key不能重复
s = set([1, 2, 3])

#可变参数
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
print calc(1,2,3)


#命名参数
def person(name,age,**kw):
    print(name,age,kw)
person('Bob',35,gener='M',job='Engineer')


def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num * product)
print (fact(5))



L=[]
n=1
while n<=99:
    L.append(n)
    n=n+2
print(L)


#切片  L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3
L=list(range(100))
print(L[10:13])
print(L[-10:])
print(L[10:20])

#实现一个trim()函数，去除字符串首尾的空格
def trim(s):
    while s[0:1]==' ':
      s=s[1:]
    while s[-1:]==' ':
        s=s[:-1]
    return s
if trim('hello   ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('   hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


#使用迭代查找一个list中最小和最大值
def findMinAndMax(L):
    if len(L) == 0:
        min=None
        max=None
    else:
         min=L[0]
         max=L[0]
    for a in L:
        if a<=min:
            min=a
        if a>max:
            max=a
    return('min=',min,'max=',max)
print(findMinAndMax([5,2]))

#列表生成式
print([x*x for x in range(1,11) if x%2==0])
print([m+n for m in 'ABC' for n in 'XYZ'])


#非字符串类型没有lower()方法  内建的isinstance函数可以判断一个变量是不是字符串
L1=['Hello','World',18,'Apple',None]
L2=[]
for x in L1:
    if isinstance(x,str)==True:
        L2.append(x.lower())
    else:
        pass
print(L2)

#高阶函数
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
#map()传入的第一个参数是f，即函数对象本身
L=list(map(str,[1,2,3,4,5,6]))
print(L)
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


from functools import reduce
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
def char2int(s):
    def fn(x,y):
        return 10*x+y
    def char2num(s):
        return digits[s]
    return reduce(fn,map(char2num,s))
print(char2int('13579'))


#返回函数   把函数作为结果值返回
def calc_num(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
f=calc_num(1,3,5,7,9)
print(f())


#匿名函数
L=list(filter(lambda x:x%2==1,range(1,20)))
print(L)


#装饰器
def log(func):
    def wrapper(*args,**kw):
        print('call %s():'% func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now(name=None):
    print('2018-12-27: %s' % name)

now()
now(name='123')


#模块
import sys
def test():
    args=sys.argv
    if len(args)==1:
        print('Hello,World!')
    elif len(args)==2:
        print('Hello,%s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

#面向对象
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def get_score(self):
        if self.score>=90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'

bart=Student('Aime',67)
print(bart.get_score())

#访问限制
class Student(object):
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender

    def set_gender(self,gender):
        if gender=='male' or gender=='female':
            self.__gender=gender
        else:
            raise ValueError('Bad Input')
    def get_gender(self,gender):
        return self.__gender

bart=Student('Bart','male')


#实例属性与类属性
class Student(object):
    count=0                 #类属性

    def __init__(self,name):        #构造函数__init__
        self.name=name
        Student.count=Student.count + 1

bart=Student('aaa')         #创建实例
lisa=Student('bbb')         #创建实例
print(Student.count)
print(bart.count)


class Student(object):
    pass

s=Student()     #创建实例
s1=Student()
def set_age(self,age):      #定义一个函数作为实例方法
    self.age=age

Student.setage=set_age     #给class绑定方法

s.setage(40)       #调用实例方法
print(s.age)
s1.setage(30)
print(s1.age)


#当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至except语句块，执行完except后，如果有finally语句块，则执行finally语句块（可以没有finally语句）
try:
    print('try...')
    r = 10/int('a')
    print('result:',r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')


#跨越多层调用
import logging
def foo(s):
    return 10/int(s)

def bar(s):
    r=foo(s) * 2
    return r
def main():
    try:
        bar(0)
    except Exception as e:
        print('Error:',e)
        logging.exception(e)
main()
print('end')


#抛出错误
def Error(ValueError):
    pass

def foo(s):
    r=int(s)
    if r==0:
        raise ValueError('invalid value: %s' % s)
    return 10/r
foo(0)


#读文件
f=open('/Users/aimee/Desktop/Hello.txt','r')
print(f.read())

#写文件
with open('/Users/aimee/Desktop/Hello.txt','a') as f:
    f.write('lallala')


import os
print(os.path.join('/Users/aimee/PycharmProjects/TU','testdir'))
os.rmdir('/Users/aimee/PycharmProjects/TU/testdir')


#json化
import json
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
s=Student('Bob',22,88)

def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
print(json.dumps(s,default=student2dict))


#进程和线程
#fork（）系统调用
import os
print('Process (%s) start...' % os.getpid())
pid=os.fork()
if pid==0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just create a child process (%s).' % (os.getpid(),pid))



#urllib
import urllib2
f=urllib2.Request("https://www.douban.com")
response=urllib2.urlopen(f)
print(response.read())


from PIL import Image,ImageFilter
#打开jpg图像文件
im=Image.open('/Users/aimee/Desktop/3.jpg')
#获取图像尺寸
w,h=im.size
print('Original image size:%sx%s' % (w,h))
#缩放到50%
im.thumbnail((w//2,h//2))
#把缩放后的图像用jpeg格式保存
im.save('/Users/aimee/Desktop/test1.jpeg')
#应用模糊滤镜
im2=im.filter(ImageFilter.BLUR)
im2.save('/Users/aimee/Desktop/test2.jpeg')


#PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
#随机字母
def rndChar():
    return chr(random.randint(65,90))
#随机颜色1
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
#随机颜色2
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
#240*60
width=60*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))
# 创建Font对象：
font=ImageFont.truetype('Arial.ttf',36)
#创建Draw对象：
draw=ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
#输出文字
for t in range(4):
    draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
#模糊
image=image.filter(ImageFilter.BLUR)
image.save('/Users/aimee/Desktop/code.jpg')


#requests   get请求
import  requests
# r=requests.get('https://www.douban.com/',params={'q':'python','cat':'1001'})
# print(r.url)


#post请求
r=requests.post('https://accounts.douban.com/login',data={'form_email':'abc&example.com','form_password':'123456'})
params={'key':'value'}
r1=requests.post(r.url,json=params)
print(r1)


from Tkinter import *
import tkMessageBox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alterButton = Button(self,text='Send',command=self.hello)
        self.alterButton.pack()

    def hello(self):
        name=self.nameInput.get() or 'World'
        messagebox.showinfo('Message','Hello, %s' % name)
app=Application()
app.master.title('Hello,World!')
app.mainloop()


#客户端
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer=[]
while True:
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)
s.close()
header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('/Users/aimee/Desktop/sina.html','wb') as f:
    f.write(html)


#发邮件
import smtplib
from email.mime.text import MIMEText
import threading
import time, datetime

mailto_list=["1069923094@qq.com"] #里面是对方的邮箱
#-----------QQ邮箱发送设置----------------------
mail_server="smtp.qq.com"#以qq邮箱为例子，里面是QQ邮箱的服务，换成其他邮箱需要更改服务
mail_user="1069923094@qq.com"#这是QQ邮箱的账号
mail_pass="ctacufjpmpafbcfd"#如果是其他的可以直接填上密码，如果用qq之类的，或者邮箱未开服务，会提醒你打开下面的链接
#QQ邮箱需要去官方打开服务：http://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256
def send_mail(to_list, sub, content):
    msg = MIMEText(content,'plain','utf-8')
    msg["Accept-Language"]="zh-CN"
    msg["Accept-Charset"]="ISO-8859-1,utf-8"
    msg['Subject'] = sub
    msg['From'] = mail_user
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_server)
        server.starttls()
        server.login(mail_user, mail_pass)
        server.sendmail(mail_user, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

def getDate():
    # return str(datetime.datetime.utcfromtimestamp(time.time())+datetime.timedelta(hours=8))
    # return str(datetime.datetime(2018,1,[16,[17,[33,[0,[0,[0,0]]]]]]))
    return (datetime.datetime.now() + datetime.timedelta(minutes=3)).strftime("%Y-%m-%d %H:%M:%S")


def send_warning_mail(title, info):
    nowTime = getDate()
    try:
        t = threading.Thread(target=send_mail, args=(mailto_list, title, str(nowTime) + " | " + str(info)))
        t.start()
    except:pass
    # send_mail(mailto_list, "mysql异常", info)

if __name__ == '__main__':
    send_warning_mail("this is title", "\nthis is content")
#     print 111

'''


import requests

url = "http://192.168.31.178:8080/member/login"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"mobile\"\r\n\r\n13026171123\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"zone\"\r\n\r\n86\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n123456\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"deviceId\"\r\n\r\n1234523123231\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"accessToken\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"openid\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Cache-Control': "no-cache",
    'Postman-Token': "f7236b78-6dfe-f594-12c4-58d975aa9fc1"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
