#!/usr/bin/python3
from sys import argv                # for arguments
from datetime import datetime       # for date printing
import nltk                         # natural language tookkit
import pymysql

print ("Time is: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
if len(argv) < 2:
    print("Missing arguments")
    exit()

# print current time to file to prove we ran
file = open("log.log", "a")
file.write("Time is: %s - %s\n" % (datetime.now(),  argv[1]))
file.close()

#print "\nArg1: ", argv[1:]  # Will print out all arguments starting at 1

# echo the sentence
sentence = argv[1]
#sentence = """At eight o'clock on Thursday morning"""   # debugging
print ("Sentence is: %s" % sentence)

# separates sentence into tokens or individual words
tokens = nltk.word_tokenize(sentence)
print ("\nTokens %r\n" % tokens)

# identifies each token to a part of speech
tagged = nltk.pos_tag(tokens)
print ("Tagged words: %r\n" % tagged[0:6])


def db_run_querey(db, query):
    # https://stackoverflow.com/a/13846183
    config = {
      'user': 'nick',
      'passwd': 'harvey',
      'host': 'database.nkren.net',
      'db': db,
    }
    try:
      conn = pymysql.connect(**config)
    except Exception as e:
        print ("error ", e)
        return 1
    else:
        cur = conn.cursor()
        try:
            cur.execute(query)
        except Exception as e:
            print("An error occured when executing query")
            print("\tThe query: %r " % query)
            print (e)
            return 1
        else:
            rtn_list = []
            #print (cur.fetchall())
            for response in cur:
                #print("Response: %r\tType: %r" % (response, type(response)))   # response is a tuple
                print(response)
                rtn_list.append(response[0])
            #print ("rtn_list: %r" % rtn_list)
        cur.close()
        conn.close()
    return rtn_list
    

# SQL reference queries
# SELECT TABLE_SCHEMA, TABLE_NAME FROM information_schema.tables where table_schema='drugsdatabase';
# SELECT table_name, column_name FROM `COLUMNS` where table_schema = 'drugsdatabase' and table_name = 'marketingstatus'
# SELECT table_name, column_name FROM `COLUMNS` where table_schema = 'drugsdatabase'

# SELECT
# FROM
# WHERE
sql_output = {}
sql_output['SELECT'] = ""
sql_output['FROM']   = ""
sql_output['WHERE']  = ""
        
#db = "drugsdatabase"
db = "world"
tables = db_run_querey(db, "SELECT table_name FROM information_schema.tables where table_schema='" + db + "';")
print ("--------------------")

db_schema2 = {}
for t in tables:
    db_schema2[t] = {}  # create dictionary of attributes
    #print (i)
    attributes = db_run_querey('information_schema', "SELECT column_name FROM `COLUMNS` where table_schema = '" + db + "' and table_name = '" + t + "'")
    for a in attributes:
        db_schema2[t][a] = a
print ("------")
#print("Post table grab: %s" % db_schema2)       # debugger


# depending on how the disctionary is sorted this may return different results
# stops on first hit. Problem if multiple tables use the same attribute
def find_attribute(keyword, schema):
    # is keyword a table?
    if keyword in schema:
        print("%s is a table name" % keyword)
    
    # is keyword a attribute of a table
    match_found = False
    rtn_list = []
    for t in schema:    # loop through tables
        #print ("table: %s" % t)                                             # debugger
        for a in schema[t]:     # search attributes in table
            #print ("attribute: %s" % a)                                     # debugger
            if keyword == a:
                print("Found match for %s in table %s" % (keyword, t))      # debugger
                match_found = True
                rtn_list.append((t,a))
    if not match_found:
        print ("No match found for %s" % keyword)
        return 0
    #print(rtn_list)
    return rtn_list

g = find_attribute("Capital", db_schema2)
print (g)

find_attribute("Language", db_schema2)
find_attribute("Population", db_schema2)

find_attribute("Strength", db_schema2)



exit()  # not ready yet
# Run output SQL query
db_run_querey(db, sql_output['SELECT'] + sql_output['FROM'] + sql_output['WHERE'])






exit()
db_schema = { 
            "Table1" :
              {
                  "Movies": ["Movies", "Films", "Film"],
                  "c2": ["c2", "a1", "a2"],
                  "c3": ["c3"],
                  "c4": ["c4"]
              },
            "Table2" : ["c1", "a1", "a2"]
            }

db_schema_curr = { 
            "Table1" :
              {
                  "Movies": "Movies",
                  "c2": "c2",
                  "c3": "c3",
                  "c4": "c4"
              },
            "Table2" : ["c1", "a1", "a2"]
            }


print ("\n\n")
print (db_schema)