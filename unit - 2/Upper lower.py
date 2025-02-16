string = input ()
re_str = ""
for i in string :
    if i.isupper() :
        re_str += i.lower()
    else:
        re_str += i.upper()
print("input : " + string)
print("output : " + re_str)
