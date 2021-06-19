from notecard import Card
from data import Data
from flask import Flask, request, jsonify

#initiate Flask app
app = Flask(__name__)
app.config["DEBUG"] = True

d = Data()

#Home route
@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to Notable</h1><p>This site is a prototype for a flash card studying application.</p>"

@app.errorhandler(404)
def page_not_found(e):
        return "<h1>404</h1><p>The resource could not be found.</p>", 404

#Return card search results
@app.route('/api/v1/tables', methods=['GET'])
def search():
    query_parameters = request.args
    category = query_parameters.get('category')
    to_filter = []

    if category:
        to_filter.append(category)
        results = d.getAllByCat(d.cur,to_filter)
    else:
        results = d.getAll(d.cur,'cards')

    questions = []
    for row in results:
        questions.append(row[0])
        questions.append(row[1])
    return jsonify(questions)

# questions = []
# for row in d.getAll(d.cur, 'cards'):
#     questions.append(Card(row[0], row[1]))

# For reading from Text
# f = open('text.txt','r')
# for i in range(1,4):
#     questions.append(Card(f.readline(),f.readline()))

# for q in questions:
#     q.reveal()
#     print('')

# quit()
app.run()
