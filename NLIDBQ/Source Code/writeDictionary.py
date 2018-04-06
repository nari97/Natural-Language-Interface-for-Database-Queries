import dbm

table_data = dbm.open('table_data','c')
tables = dbm.open('tables','c')
escape_words = dbm.open('escape_words','c')

def createDictStudent(tablename,string,field,table_data):
    
    table_data[tablename + " " + string] = field
    #table_data[string + " " + tablename] = field
    table_data[string + " " + tablename + "s"] = field
    table_data[string + " of " + tablename] = field
    table_data[string + " of " + tablename + "s"] = field
    table_data[string + "s" + " of " + tablename] = field
    table_data[string + "s" +  " of " + tablename + "s"] = field
    table_data[tablename + "'s " + string] = field
    table_data[tablename + "s " + string + "s"] = field
    table_data[tablename + "s " + string] = field
    table_data[tablename + " " + string + "s"] = field
    table_data[string] = field

    return table_data

table_data = createDictStudent("student","usn","attribute_Student_usn",table_data)
table_data = createDictStudent("student","name","attribute_Student_name",table_data)
table_data = createDictStudent("student","phone number","attribute_Student_phone",table_data)
table_data = createDictStudent("student","scheme","attribute_Student_scheme",table_data)
table_data = createDictStudent("student","all","Student.*",table_data)


table_data = createDictStudent("teacher","id","attribute_Teacher_id",table_data)
table_data = createDictStudent("teacher","name","attribute_Teacher_name",table_data)
table_data = createDictStudent("teacher","phone number","attribute_Teacher_phone",table_data)
table_data = createDictStudent("teacher","all","Teacher.*",table_data)


table_data = createDictStudent("scheme","name","attribute_Scheme_name",table_data)
table_data = createDictStudent("scheme","year","attribute_Scheme_year",table_data)
table_data = createDictStudent("scheme","all","Scheme.*",table_data)


table_data = createDictStudent("subject","name","attribute_Subject_name",table_data)
table_data = createDictStudent("subject","scheme","attribute_Subject_scheme",table_data)
table_data = createDictStudent("subject","all","Subject.*",table_data)

table_data["students"] = "Student.*"
table_data["student"] = "attribute_Student_name"

table_data["teachers"] = "Teacher.*"
table_data["teacher"] = "attribute_Teacher_name"

#table_data["scheme"] = "Scheme.*"
table_data["schemes"] = "Scheme.*"

table_data["subject"] = "attribute_Subject_name"
table_data["subjects"] = "Subject.*"

table_data["teaches"] = "attribute_Subject_teaches"

table_data.close()



