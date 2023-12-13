from whoosh import index
from whoosh.query import *
from whoosh.qparser import QueryParser, OrGroup, MultifieldParser
class MyIndexReader:
    def __init__(self, parser_type):
        path_dir= "index"
        myindex = index.open_dir(path_dir)
        self.searcher = myindex.searcher()
        if parser_type == "single":
            self.parser = QueryParser("game_desc", schema=myindex.schema, group=OrGroup)
        if parser_type == "multi":
            fieldsboots = {
                "game_name":0.2,
                "game_desc":0.6,
                "tags":0.2,
            }
            fields = list(fieldsboots.keys())
            self.parser = MultifieldParser(fields, schema=myindex.schema, group=OrGroup, fieldboosts=fieldsboots)
    def search(self, query:str):
        myquery = self.parser.parse(query.strip().lower())
        print(f"query: {myquery.all_terms()}")
        return self.searcher.search(myquery)
    