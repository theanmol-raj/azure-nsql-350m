from flask import Flask, jsonify, request
from src.components.model_loader import NsqlModel

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'message': 'Hello, welcome to your Flask API!'})

@app.route('/test', methods=['GET'])
def helxlo():
    return jsonify({'message': 'Hello, welcome to your Flask API!'})

@app.route('/test', methods=['POST'])
def getPromptResult():
    data = request.get_json()
    model = NsqlModel()
    response = model.predict(data['prompt'])
    return jsonify ({'message' : response})
    

if __name__ == '__main__':
    app.run(debug=True)


# (async () => {
#   const rawResponse = await fetch('http://127.0.0.1:5000/test', {
#     method: 'POST',
#     headers: {
#       'Accept': 'application/json',
#       'Content-Type': 'application/json'
#     },
#     body: JSON.stringify({prompt : `CREATE TABLE stadium (
#     stadium_id number,
#     location text,
#     name text,
#     capacity number,
# )

# -- Using valid SQLite, answer the following questions for the tables provided above.

# -- how many stadiums in total?

# SELECT`})
#   });
#   const content = await rawResponse.json();

#   console.log(content);
# })();