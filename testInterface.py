# coding=utf8

import requests

headers={'token':'6f46add1-aba0-494d-a58a-a646122b5cec'}

#获取宝宝信息
def list():
    list_body={'familyId':'14963'}
    response = requests.post("http://192.168.31.179:8082/family/babies",data=list_body,headers=headers)
    retTxt = response.text
    print(retTxt)

#增加宝宝
def add():
    add_body={'babyName':'123',
              'babyIcon':' ',
              'birthday':'2018-02-01',
              'jender':'0',
              'memberId':'14864',
              'familyId':'14963'}
    add_url='http://192.168.31.179:8082/family/addBaby'
    response = requests.post(add_url,data=add_body,headers=headers)
    retTxt = response.text
    print(retTxt)


#修改宝宝信息
def modify():
    modify_body={'babyName':'123哈哈',
              'babyIcon':' ',
              'birthday':'2018-02-01',
              'jender':'1',
              'memberId':'14864',
              'familyId':'14963',
              'id':'15168'}
    modify_url='http://192.168.31.179:8082/family/modifyBaby'
    response = requests.post(modify_url,data=modify_body,headers=headers)
    retTxt = response.text
    print(retTxt)

#删除宝宝
def delete():
    delete_body = {'memberId': '14864',
                'familyId': '14963',
                'babyId': '15168'}
    delete_url = 'http://192.168.31.179:8082/family/deleteBaby'
    response = requests.post(delete_url, data=delete_body, headers=headers)
    retTxt = response.text
    print(retTxt)


list()
# delete()
# modify()
# add()






