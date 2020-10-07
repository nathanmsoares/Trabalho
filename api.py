import requests
import json
import random

ZABIX_ROOT = 'http://192.168.0.3/zabbix'
url = ZABIX_ROOT + '/api_jsonrpc.php'

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

########################################
# host.get
########################################
# payload = {
#     "jsonrpc" : "2.0",
#     "method" : "host.get",
#     "params": {
#       'output': [
#           'hostid',
#           'name'],
#     },
#     "auth" : res['result'],
#     "id" : 2,
# }

#pegar usuários de um grupo
# payload = {
#     "jsonrpc": "2.0",
#     "method": "user.get",
#     "params": {'usrgrpids': 7},
#     "auth" : res['result'],
#     "id" : 2
# }


#### criar usuários
for i in range(10000):
    y = str(random.randint(1,1000000))
    payload = {
        "jsonrpc": "2.0",
        "method": "user.create",
        "params": {
            "alias": y,
            "passwd": y,
            "usrgrps": [
                {
                    "usrgrpid": "7"
                }
            ],
            "user_medias": [
                {
                    "mediatypeid": "1",
                    "sendto": [
                        "support@company.com"
                    ],
                    "active": 0,
                    "severity": 63,
                    "period": "1-7,00:00-24:00"
                }
            ]
        },
        "auth": res['result'],
        "id": 1
    }

#### achar grupo pela id do usuário
# payload = {
#     "jsonrpc": "2.0",
#     "method": "usergroup.get",
#     "params": { 'output': 'extends',
#                 'userids': 'nathan'},
#     "auth" : res['result'],
#     "id" : 2
# }



#### Deletar usuarios


    res2 = requests.post(url, data=json.dumps(payload), headers=headers)
    print('teste', json.dumps(payload))
    res2 = res2.json()
    print('host.get response')
    #print(res2)
    x = res2['result']
    #print(x)
    lista_temporaria = []
    # for i in x:
    #     print(i.items())
    # print('lista', lista_temporaria)








#### LOGOUT
payload = {
    "jsonrpc": "2.0",
    "method": "user.logout",
    "params": [],
    "id": 1,
    "auth": res['result']
}