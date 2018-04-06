import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer

queries = ["select all from student","select name of student from student","select name from student where name of teacher equals name of student","select name of student where name of student equals name of teacher and name of student is Narayanan"]

stop_words = set(stopwords.words('english'))
stop_words.remove("all")
stop_words.remove("of")
stop_words.add("show")
stop_words.remove("where")
stop_words.add("equals")


for i in queries:
    
    toke = word_tokenize(i)
    sent = [w for w in toke if not w in stop_words]
    print nltk.pos_tag(sent)