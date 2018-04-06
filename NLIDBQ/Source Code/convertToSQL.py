import MySQLdb as sql
import dbm
import sys

def removeEscapeWords(string,escapeWords):
    tokens = string.split()															#Splits the string
    toke = string.split()
    newString = ""
    for i in tokens:
        if escapeWords.has_key(i): 
            toke.remove(i)															#Removes escape words
            
    for i in toke:
        newString = newString + i + " "										#Combines tokens

    newString = newString[0:len(newString)-1]
    return newString

def splitString(string):															#Function is used
	tokens = string.split()															#to remove last word
	newString = ""
	#print tokens
	for i in range(0,len(tokens)-1):
		newString = newString + tokens[i] + " "
	return newString

def removeWords(mainString,subString):												#Function is used
	i = mainString.find(subString,0,len(mainString))								#to remove words found
	mainString = mainString[:i] + mainString[i + len(subString) + 1 : ]				#in respective dictionaries
	return mainString

def removeQuotedWords(mainString):													#Function is used
	i = -1
	quoted = ""
	if mainString.find("\"",0,len(mainString))!=-1:			
		i = mainString.find("\"",0,len(mainString))									#to remove words in
		quoted = mainString[i:]														#quotes
		mainString = mainString[:i]
	return i,quoted,mainString

def checkForeignKey(table_names,newString):
	i = newString.find("_",0,len(newString))
	j = newString.find("_",i+1,len(newString))

	tName = newString[i+1:j]
	
	if tName not in table_names:
		table_names.append(tName)

	tName = newString[0:len(newString)-1]

def updateAllAttributes(attributes,tableString):
	if(len(attributes))==1:
		for a in range(0,len(attributes)):
			newString = attributes[a]
			i = newString.find("_",0,len(newString))
			j = newString.find("_",i+1,len(newString))

			attributes[a] = newString[:i+1] + tableString + newString[j:]

			print newString	

dict = dbm.open("table_data")
escapeWords = dbm.open("escape_words")
tables = dbm.open("tables")
attributes = []
table_names = []
where_clause = []
whereFlag = 0

nlQuery = raw_input("Enter Query : ")
quotedFlag,quotedWords,nlQuery = removeQuotedWords(nlQuery)
#print quotedFlag
nlQuery = removeEscapeWords(nlQuery,escapeWords)
print "After removing escape words : " +  nlQuery + "\n"
newString = nlQuery

while (len(newString)>1):

	print "After removing last word : " + newString 

	#print "After removing last word : " + newString
	#print  

	if newString=="where":										#checks for where
		#print "Removing : " + newString
		print "\nWhere keyword found, removing where keyword"
		newString = removeWords(nlQuery,newString)
		nlQuery = newString
		whereFlag = 1
		print "New string is now : " + nlQuery + "\n"											#if where is found sets whereFlag = 1
		#print newString

	if whereFlag==1:		
																#for every string after where
		if dict.has_key(newString):		
			#print "Entering where"							
			#print dict[newString]
			#print "Removing : " + newString
			print "\nMatch found in dictionary for : " + newString + " corresponds to : " + dict[newString]
			print "Removing : " + newString + "\n"
			where_clause.append(dict[newString])
			#checkForeignKey(table_names,dict[newString])				#adds to dictionary
			newString = removeWords(nlQuery,newString)
			nlQuery = newString
			print "New string is now : " + nlQuery + "\n"
			continue
			#print newString 
	
	else:														#For everything before where
		if dict.has_key(newString) == True:
			#print dict[newString]
			print "\nMatch found in dictionary for : " + newString + " corresponds to : " + dict[newString]
			print "Removing : " + newString + "\n"
			attributes.append(dict[newString])					#Used to add to attributes dict
			newString = removeWords(nlQuery,newString)
			nlQuery = newString
			print "New string is now : " + nlQuery + "\n"
			continue


	if (len(newString.split())==1) or len(newString.split())==2:

		if whereFlag==1:
			if dict.has_key(newString):
				where_clause.append(dict[newString])
				#checkForeignKey(table_names,dict[newString])
		else:

		#	if tables.has_key(newString):
		#		table_names.append(tables[newString])

			if dict.has_key(newString):
				attributes.append(dict[newString])


	newString = newString.strip()
	newString = splitString(newString)
	newString = newString.strip()
	#print "Next Iteration"

#print where_clause


print "Attributes : " + str(attributes)


for newString in attributes:
	checkForeignKey(table_names,newString)

if len(table_names)==1:
	updateAllAttributes(where_clause,table_names[0])

for newString in where_clause:
	checkForeignKey(table_names,newString)

 
	
print "Tables : " + str(table_names)
print "Where_Clauses : " + str(where_clause)
queryString = "select "
for i in attributes:
	queryString = queryString + i + ","
queryString = queryString[0:len(queryString)-1]
queryString = queryString + " from "
for i in table_names:
	queryString = queryString + i + ","

queryString = queryString[:len(queryString)-1]

#print queryString

if whereFlag==1:
	queryString = queryString + " where "
	if quotedFlag >=0:
		for i in where_clause:
			queryString = queryString + i 

		queryString = queryString + " = " + quotedWords
	else:

		i = 0
		while i <len(where_clause):
			queryString = queryString + where_clause[i] + " = " + where_clause[i+1] + " and "
			i = i+2

		queryString = splitString(queryString)
		queryString = queryString[0:len(queryString)-1]

#fin = queryString.find(".",len(queryString),len(queryString))
#queryString = queryString[0:fin]
print queryString


#print where_clause
#print quotedWords






