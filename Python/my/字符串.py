
str = "hello world ha ha ha ha ha"

# mystr.find(str, start=0, end=len(mystr))  检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1
# mystr.index(str, start=0, end=len(mystr))     跟find()方法一样，只不过如果str不在 mystr中会报一个异常.
# mystr.count(str, start=0, end=len(mystr))   返回 str在start和end之间 在 mystr里面出现的次数
# mystr.replace(str1, str2,  mystr.count(str1))     把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.
# mystr.split(str=" ", 2)       以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
# mystr.capitalize()        把字符串的第一个字符大写
# mystr.title()             把字符串的每个单词首字母大写
# mystr.startswith(obj)     检查字符串是否是以 obj 开头, 是则返回 True，否则返回 False
# mystr.endswith(obj)       检查字符串是否以obj结束，如果是返回True,否则返回 False.
# mystr.lower()             转换 mystr 中所有大写字符为小写
# mystr.upper()             转换 mystr 中的小写字母为大写
# mystr.ljust(width)        返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
# mystr.rjust(width)        返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
# mystr.center(width) 
# mystr.lstrip() rstrip()  strip()   删除mystr 字符串 左边 /右边 /  两端的空白字符

str = str.capitalize()
str = str.replace("ha","wa")
print(str)
str = str.title()
str = str.replace("ha","wa",2)

print(str)
str.split(" ")
print(str)
