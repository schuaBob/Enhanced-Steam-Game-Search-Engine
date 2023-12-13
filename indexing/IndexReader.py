from whoosh import index
from whoosh.query import *
from whoosh.qparser import QueryParser, OrGroup
class MyIndexReader:
    def __init__(self):
        path_dir= "index"
        myindex = index.open_dir(path_dir)
        self.searcher = myindex.searcher()
        self.parser = QueryParser("game_desc", schema=myindex.schema, group=OrGroup)
    def search(self, query:str):
        myquery = self.parser.parse(query.strip().lower())
        result = self.searcher.search(myquery)
        print(f"query: {myquery.all_terms()}")
        for res in result:
            print(f"name: {res['game_name']}, score:{res.score}")
            # print(res['game_desc'])
    