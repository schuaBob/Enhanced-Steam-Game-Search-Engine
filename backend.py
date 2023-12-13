from flask import Flask
from indexing.IndexReader import MyIndexReader

app = Flask(__name__)
indexReader = MyIndexReader()

@app.route("/search?q=<query>")
def search(query):
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
    return list_dicts