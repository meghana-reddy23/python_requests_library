import requests

"""
#to send request
r=requests.get("https://eo9ditdu352anek.m.pipedream.net")
"""

"""
#get response in text and json formats
r=requests.get("https://reqres.in/api/users/1")
print(r)
print(r.text)
print("\n\n")
a=r.json()
print(a["data"]["first_name"])
"""

"""
#send url prameters
r=requests.get("https://eo9ditdu352anek.m.pipedream.net?key1=value1&key2=value2")
"""

"""
# send parameters using dict

payload={'first':'one','second':'two'}

r=requests.get("https://eo9ditdu352anek.m.pipedream.net",params=payload)
"""

"""
#sending custom headers and modifying existing headers
h={'mytoken': '45486926u428hteghabfkadbfiebgbrskhvbskhfgb','user-agent': 'fake-agent'}
r=requests.get("https://eo9ditdu352anek.m.pipedream.net",headers=h)
"""

"""
#other requests methods
#get : to retrieve some information
r=requests.get("https://eo9ditdu352anek.m.pipedream.net")

#post: to add some new information
r=requests.post("https://eo9ditdu352anek.m.pipedream.net")

#delete: to delete information on server
r=requests.delete("https://eo9ditdu352anek.m.pipedream.net")

#put: to modify info in server
r=requests.put("https://eo9ditdu352anek.m.pipedream.net")

#patch: same as put
r=requests.patch("https://eo9ditdu352anek.m.pipedream.net")
"""

"""
#sending request with json data
payload={'name':'meg','job':'ceo'}
#need this header for every request as website got updated
h={'x-api-key': 'reqres-free-v1'}
r=requests.post('https://reqres.in/api/users',json=payload,headers=h)
print(r)
print(r.text)
"""

"""
#sending form data (observer content-type for form,json,urlparameters)
payload={'name':'meghana','location':'texas'}
#to requestbin
r=requests.post('https://eo9ditdu352anek.m.pipedream.net',data=payload)
r=requests.post('https://eo9ditdu352anek.m.pipedream.net',json=payload)
r=requests.post('https://eo9ditdu352anek.m.pipedream.net',params=payload)
#to http bin
r2=requests.post('https://httpbin.org/post',data=payload)
print(r2.text)
"""

"""
#send file
files={'file':open("sample.txt","rb")}
r=requests.post('https://eo9ditdu352anek.m.pipedream.net',files=files)
"""

"""
#Saving file from response
r=requests.get("https://httpbin.org/image/jpeg")
print(r.headers)
with open('myimage.jpeg','wb') as f:
    for chunk in r.iter_content(chunk_size=500):
        f.write(chunk)
"""

#exception
"""
r=requests.get("https://httpbin.org/status/505")
try:
    r.raise_for_status()
except requests.exceptions.HTTPError:
    print("HTTP Error")
print(r)
"""
"""
#connection error exception
try:
    r=requests.get("https://sjkfbadkhbvnvda.com")
except requests.exceptions.ConnectionError:
    print("Connection Error")
"""
"""
#connection timeout exception
try:
    r=requests.get("https://httpbin.org/",timeout=1)
except requests.exceptions.ConnectionTimeout:
    print("Connection Timeout")
"""

"""
#response timeout exception
try:
    r=requests.get("https://httpbin.org/delay/4",timeout=1)
except requests.exceptions.readTimeout:
    print("Response from server Timeout")
"""

#authentication
from requests.auth import HTTPBasicAuth
r=requests.get("https://httpbin.org/basic-auth/user/passwd",auth=HTTPBasicAuth("user","passwd"))
print(r)


