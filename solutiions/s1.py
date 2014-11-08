# coding=utf-8
__author__ = 'gk23<aoaogk@gmail.com>'

# solution for problem 0：http://www.pythonchallenge.com/pc/def/274877906944.html
print 2 ** 38

# ==============================================
# solution for problem 1：http://www.pythonchallenge.com/pc/def/ocr.html
str = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
      bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
      sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

res = ""
for s in str:
    if (ord(s) >= ord('a')):
        res = res + chr(ord('a') + (ord(s) + 2 - ord('a')) % 26)
    else:
        res = res + s
print res

# solution 2 for problem 1
import string

t = string.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')

print str.translate(t)

# ==============================================
# solution for problem 2：http://www.pythonchallenge.com/pcc/def/equality.html

file = open("2.txt")
try:
    text = file.read()
finally:
    file.close()
dict = {}
# solution 1
for s in text:
    if s >= 'a' and s <= 'z':
        print s,
    if (not dict.has_key(s)):
        dict[s] = 1
    else:
        dict[s] = dict.get(s) + 1
print ""
print dict
# solution 2
print "".join([char for char in text if char.isalpha()])
# solution 3
print filter(lambda x: x in string.letters, text)

# ==============================================
# solution for problem 3：http://www.pythonchallenge.com/pc/def/linkedlist.php
import re
text = open("3.txt").read()
re_str = "[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]"

## match 只从开头匹配，否则应该用search
# print re.compile(re_str1).match(text)

# 如果正则中有括号代表group1，findall则只返回括号的内容
print "".join(re.findall(re_str,text))
# print re.findall(re_str,text)
