import nltk
import dbm
import sys
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import MySQLdb as sql

dict1 = dbm.open("/home/nari/MySQLProject/Python/table_data")
attributes = []
table_names = []
where_attributes = []
conditions =["where","whose","under","in","belongs","which","that","who"]
fKeys = dict()
fKeyDict = []
clashes = ["name","phone number","scheme"]
whereFlag = 0
nlQuery = ""

stop_words = set(stopwords.words('english'))
stop_words.remove("all")
stop_words.remove("of")
stop_words.add("show")
stop_words.remove("where")
stop_words.add("equals")
stop_words.add("same")
stop_words.add("find")
stop_words.add("started")
stop_words.remove("which")
stop_words.remove("that")
stop_words.remove("under")
stop_words.remove("with")
stop_words.remove("who")
stop_words.remove("does")

fKeys["Student,Scheme"] = ["attribute_Student_scheme = attribute_Scheme_name"]
fKeys["Scheme,Student"] = ["attribute_Student_scheme = attribute_Scheme_name"]
fKeys["Subject,Scheme"] = ["attribute_Subject_scheme = attribute_Scheme_name"]
fKeys["Scheme,Subject"] = ["attribute_Subject_scheme = attribute_Scheme_name"]
fKeys["Teacher,Subject"] = ["attribute_Subject_teaches = attribute_Teacher_id"]
fKeys["Subject,Teacher"] = ["attribute_Subject_teaches = attribute_Teacher_id"]

def fKeyHandle():
    if(len(table_names)>1):
        str = table_names[0] + "," + table_names[1]
        str = str.strip()
        #print str
        if(fKeys.has_key(str)):            
            fKeyDict.append(fKeys[str]) 

def removeLastWord(str):
    toke = word_tokenize(str)
    newStr = ""
    for i in range(0,len(toke)-1):
        newStr = newStr + toke[i] + " "

    newStr = newStr.strip()

    return newStr


def removeEscapeWords(str):
    toke = word_tokenize(str)

    newToke = [w for w in toke if not w in stop_words]
    newStr = ""
    for i in newToke:
        newStr = newStr + i + " "

    newStr = newStr.strip()

    return newStr

def removeMatchedWords(str,match):
    i = str.find(match,0,len(str))
    newStr = str[0:i] + str[(i+len(match)):]
    newStr = newStr.strip()
    return newStr

def getDepartment(str):
    #print "\ngetDept " + str
    if(str.find("_",0,len(str))>0): 
        i = str.find("_",0,len(str))
        j = str.find("_",i+1,len(str))
        newStr = str[i+1:j]
        newStr = newStr.strip()
        return newStr
    elif (str.find("*",0,len(str))>0):
        i = str.find("*",0,len(str))
        newStr = str[:i-1]
        #print newStr
        return newStr

    else:
        return ""


def constructQuery():
    query = "select "

    for i in attributes:
        query = query + i + ","

    query = query[0:len(query)-1]

    query = query + " from "

    for i in table_names:
        query = query + i + ","

    query = query[0:len(query)-1]

    if whereFlag == 1:
        query = query + " where "
        i = 0
        while i<len(where_attributes):
            query = query + where_attributes[i] + " = " + where_attributes[i+1] + " and "
            i = i + 2
        query = query[0:len(query)-4]


    if len(fKeyDict)>0:
        query = query + "and " + str(fKeyDict[0])[2:-2]
    return query

def correctClash(att):
    dept = getDepartment(attributes[0])
    
    #print dept

    i = att.find("_",0,len(att))
    j = att.find("_",i+1,len(att))

    newAtt = att[0:i+1] + dept + att[j:]
    #print newAtt
    where_attributes.append(newAtt)



f = open ("/home/nari/MySQLProject/Python/attr.txt","w")
for i in range(1,len(sys.argv)):
    nlQuery = nlQuery + sys.argv[i] + " "
#print nlQuery
nlQuery = nlQuery.strip()

nlQuery = removeEscapeWords(nlQuery)
#print nlQuery
newSent = nlQuery

while len(nlQuery)>0:

    #print "\n\nnlQuery is now : " + nlQuery

    if nlQuery=="where" or nlQuery=="whose" or nlQuery=="belong" or nlQuery == "which" or nlQuery == "that" or nlQuery == "under" or nlQuery == "with" or nlQuery == "who" or nlQuery == "does":
        whereFlag = 1
        newSent = removeMatchedWords(newSent,nlQuery)
        #print "after removing where : " + newSent
        nlQuery = newSent
        continue

    if whereFlag==1:
        
        if dict1.has_key(nlQuery):
            if nlQuery in clashes:
                #print nlQuery
                correctClash(dict1[nlQuery])
            else:
                where_attributes.append(dict1[nlQuery])
            newSent = removeMatchedWords(newSent,nlQuery)
            nlQuery = newSent
            continue

        else:
            toke = word_tokenize(nlQuery + " is")
            #print toke
            newToke = nltk.pos_tag(toke)
            toke = newToke[0]

            #print toke[0] + " is " + toke[1]

            if toke[1] == "NNP" or toke[1]=="CD":
                where_attributes.append("\"" + toke[0] + "\"")
                newSent = removeMatchedWords(newSent,toke[0])
                #print "after removing : " + newSent
                nlQuery = newSent
                continue

    else:
        if dict1.has_key(nlQuery):
            #print nlQuery + " Matched with " + dict1[nlQuery]
            attributes.append(dict1[nlQuery])
            newSent = removeMatchedWords(newSent,nlQuery)
            nlQuery = newSent
            continue

    nlQuery = removeLastWord(nlQuery)

if len(attributes) == 0:
    for st in where_attributes:
        dept = getDepartment(st)
        at = dept + ".*"
        attributes.append(at)
        break

for i in attributes:
    dept = getDepartment(i)

    if dept not in table_names:
        table_names.append(dept)

for i in where_attributes:
    dept = getDepartment(i)

    if dept!="" and dept not in table_names:
        table_names.append(dept)


fKeyHandle()
#print attributes
#print table_names
#print where_attributes


query = constructQuery()

print query
