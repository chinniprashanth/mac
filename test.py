import urllib
import ast
import json
import pprint
import ast
input1 = raw_input("Enter the Details: ")
f =urllib.urlopen("https://api.macaddress.io/v1?apiKey=at_RzQ1chh7L4iVIDkC62etuhEt9POTD&output=json&search=44:38:39:ff:ef:57")
data = f.readline()
data = json.loads(data)
pp = pprint.PrettyPrinter(indent=2)
out= data[input1].keys()
for i in out:
    print(i.encode('ascii'))
input2 = raw_input("Enter any above details :")
pp.pprint(data[input1][input2].encode('ascii'))

