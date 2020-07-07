from requests import get

IP_API = "http://ip-api.com/json"
jsonRes = get(IP_API).json()
print (jsonRes["query"]+" ["+jsonRes["isp"]+"]\n"+jsonRes["city"]+","+jsonRes["regionName"]+","+jsonRes["country"])
