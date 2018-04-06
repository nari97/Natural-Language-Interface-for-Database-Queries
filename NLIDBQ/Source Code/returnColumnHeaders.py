import sys


str = sys.argv[1]
st = str.strip()
i = str.find("_",0,len(str))
j = str.find("_",i+1,len(str))
	#f.write(str + "\n")

newStr =  str[j+1:] + " of " + str[i+1:j]
newStr = newStr.strip()
print newStr.upper()