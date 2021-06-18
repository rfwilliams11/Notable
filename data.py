import sqlite3

con = sqlite3.connect('notable.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE cards
               (front text, back text, category text)''')

# Insert a row of data
cur.execute("INSERT INTO cards VALUES ('What is the capital of Hungary?','Budapest','Capitals')")
cur.execute("INSERT INTO cards VALUES ('What is the capital of Latvia?','Riga','Capitals')")
cur.execute("INSERT INTO cards VALUES ('What is the capital of Romania?','Bucharest','Capitals')")
cur.execute("INSERT INTO cards VALUES ('What is the capital of Moldova?','Chisinau','Capitals')")

# Save (commit) the changes
con.commit()
# Close the connection
con.close()


