#! /usr/bin/python3

print("content-type: text/html")
print()

import cgi

fs = cgi.FieldStorage()
p_no = fs.getvalue("commands")


if p_no=="SV16 FOX":
   print('''<pre>Name :sourav 
    License No :20212013
    Vehicle Type :MCWG
    Engine No : bhjik2314
    Insurance validity : 9/11/2023</pre>''')

elif p_no=="MH13 BN8454":
    print('''<pre>Name :gourav 
    License No :20219864
    Vehicle Type :LMV
    Engine No : khgt5677
    Insurance validity : 9/11/2026</pre>''')

else:
    print("no data available")
