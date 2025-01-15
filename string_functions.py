#endswith string
str = "I am studying python"
print(str.endswith("app"))
print(str.endswith("hon"))

#capitalize string
str1 = "my name is prekshya"
print(str.capitalize())

str2 = "my name is prekshya"
str2=str.capitalize()
print(str2)

#replace string
str3 ="my name is prekshya"
print(str3.replace("m","q"))
print(str3.replace("my","you"))

#find string
str4 = "I am studying python "
print(str4.find("o")) # if we search for which do not exist output will be always -1.

#count string
str5 = "hello world"
print(str5.count("o"))


#wap to input users name and print its length
'''input("Enter your name:")
print("Length of your name is",len(name))'''

#wap to find the occurance of $ in a string
str6 = "$i $am $prekshya"
print(str6.count("$"))