import requests
import json
import random

zabbix = 'http://192.168.0.3/zabbix'
url = zabbix + '/api_jsonrpc.php'

########################################
# user.login
########################################
payload = {
    "jsonrpc" : "2.0",
    "method" : "user.login",
    "params": {
      'user': 'Admin',
      'password':'nathan',
    },
    "auth" : None,
    "id" : 0,
}
headers = {
    'content-type': 'application/json',
}
res  = requests.post(url, data=json.dumps(payload), headers=headers)
res = res.json()
print('user.login response')
print(res)

#  pegar usuários de um grupo
payload = {
    "jsonrpc": "2.0",
    "method": "user.get",
    "params": {"usrgrpids": "8"},
    "auth" : res['result'],
    "id" : 1
}

res2 = requests.get(url, data=json.dumps(payload), headers=headers)
#print('teste', json.dumps(payload))
res2 = res2.json()
#print((res2))
listatemporaria = [i for i in (res2['result'])]
#listatemporaria = [listatemporaria.pop(i) if i['userid'] == 1 else int(i['userid']) for i in listatemporaria]
#listatemporaria.remove(1)
#listatemporaria.remove(2)
# print(listatemporaria)
# payload =  {
#     "jsonrpc": "2.0",
#     "method": "user.delete",
#     "params": listatemporaria,
#     "auth": res['result'],
#     "id": 2
# }
res  = requests.post(url, data=json.dumps(payload), headers=headers)
res = res.json()
print(res)

#### LOGOUT
payload = {
    "jsonrpc": "2.0",
    "method": "user.logout",
    "params": {},
    "id": 3,
    "auth": res['result']
}

res  = requests.post(url, data=json.dumps(payload), headers=headers)
res = res.json()
print(res)