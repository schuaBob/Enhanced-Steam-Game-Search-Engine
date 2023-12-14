from flask import Flask, jsonify, request
from indexing.IndexReader import MyIndexReader
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/search")
def search():
    parser_type = request.args.get('parser_type')
    indexReader = MyIndexReader(parser_type=parser_type)
    query = request.args.get('q')
    myquery = indexReader.parser.parse(query.strip().lower())
    result = indexReader.searcher.search(myquery)
    print(f"query: {myquery.all_terms()}")
    list_dicts = []
    for res in result:
        list_dicts.append({
            'game_name': res['game_name'],
            'game_desc': res['game_desc'],
            'score': res.score
        })
    return jsonify(list_dicts)