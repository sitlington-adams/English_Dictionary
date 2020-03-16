#pip install mysql-connector-python
import mysql.connector
from difflib import get_close_matches
con = mysql.connector.connect( #connecting to a database, note brackets are still open)
    user="ardit700_student", #user ID
    password="ardit700_student", #Password
    host="108.167.140.122", #Host address
    database="ardit700_pm1database" #Database name
)
cursor = con.cursor() # creates a cursor element in con
query = cursor.execute("SELECT * FROM Dictionary") #Dictionary is name of the table - this * selects everything in that table
result = cursor.fetchall() #results are tuples
query3 = cursor.execute("SELECT * FROM Dictionary WHERE length(Expression) = 1") #Returns all one letter words
result3 = cursor.fetchall() #Result of query 3
#print(result3)
query4 = cursor.execute("SELECT * FROM Dictionary WHERE Expression  LIKE 'rain%'") #Returns all words that start with rain
result4 = cursor.fetchall()
user_word = input("Please enter a word: ")
query2 = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % user_word) #This will search entire dictionary for the definition of user_word. Note use of %s
result2 = cursor.fetchall()

#get_close_matches(user_word, query)


if result2:
    for x in result2:
        print(x)
else:
    print("Word not found")

#Implement typo fixes into this program.

