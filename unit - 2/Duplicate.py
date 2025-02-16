Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a,b,c = eval(input("Enter three numbers"))
... if(a==b==c):
...     print(0)
... else:
...     if(a==b):
...         print(c)
...     elif(b==c):
...         print(a)
...     elif(c==a):
...         print(b)
...     else:
