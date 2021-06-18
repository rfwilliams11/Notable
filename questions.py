from notecard import Card
import sqlite3

# one = Card("What is the capital of Hungary?","Budapest")
# two = Card("what is the capital of Latvia?","Riga")
# three = Card("What is the capital of Romania?", "Bucharest")
# four = Card("What is the capital of Moldova?", "Chisinau")

# f = open('text.txt','r')

# one = Card(f.readline(),f.readline())
# two = Card(f.readline(),f.readline())
# three = Card(f.readline(),f.readline())
# four = Card(f.readline(),f.readline())

con = sqlite3.connect('notable.db')
cur = con.cursor()

questions = []
for row in cur.execute('SELECT * FROM CARDS'):
    questions.append(Card(row[0],row[1]))

# questions = []
# for i in range(1,4):
#     questions.append(Card(f.readline(),f.readline()))

# questions = [one, two, three, four]
# questions = [one]

for q in questions:
    q.reveal()
    print('')

quit()

