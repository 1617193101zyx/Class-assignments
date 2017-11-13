Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dict1 = { 'abc': 456 }
>>> dict1
{'abc': 456}
>>> dict1['abc']
456
>>> dick1['ddd']

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    dick1['ddd']
NameError: name 'dick1' is not defined
>>>  dict1['ddd']
 
  File "<pyshell#4>", line 2
    dict1['ddd']
    ^
IndentationError: unexpected indent
>>>  dict1['abc']
 
  File "<pyshell#5>", line 2
    dict1['abc']
    ^
IndentationError: unexpected indent
>>> dict1 = { 'abc': 456 }
>>> dict1
{'abc': 456}
>>> dict1['abc']
456
>>> dict1['abc']=678
>>> dict1['abc']
678
>>> 
KeyboardInterrupt
 del dict1['abc']
>>> del dict1['abc']
>>> dict1
{}
>>> users = {
    'A':{
    'first':'yu',
    'last':'lei',
    'location':'hs',
    },
    'B':{
    'first':'liu',
    'last':'wei',
    'location':'hs',    
    },
}

>>> for username, userinfo in users.items():
    print("userid£º" + username)
	print("userinfo:" + userinfo)
	
Unsupported characters in input

>>> for username, userinfo in users.items():
	print("userid£º" + username)
	print("userinfo:" + userinfo)

	
userid£ºA

Traceback (most recent call last):
  File "<pyshell#14>", line 3, in <module>
    print("userinfo:" + userinfo)

Unsupported characters in input

>>> for username, userinfo in users.items():
	print("userid£º" + username)
	print("userinfo:" + str(userinfo))

	
userid£ºA
userinfo:{'last': 'lei', 'location': 'hs', 'first': 'yu'}
userid£ºB
userinfo:{'last': 'wei', 'location': 'hs', 'first': 'liu'}

Unsupported characters in input

>>> dict = {'Name': 'Zara', 'Age': 7}
>>> print "Value : %s" % dict.keys()
Value : ['Age', 'Name']
>>> print "Key : %s" % dict.keys()
Key : ['Age', 'Name']
>>> for key in dick.keys():
	print key


Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    for key in dick.keys():
NameError: name 'dick' is not defined
>>> for key in dict.keys():
	print key


Age
Name
>>>  for key in dict.keys():
	print dict[key]

  File "<pyshell#29>", line 2
    for key in dict.keys():
    ^
IndentationError: unexpected indent
>>> for key in dict.keys():
	print dict[key]

	
7
Zara
>>> 
