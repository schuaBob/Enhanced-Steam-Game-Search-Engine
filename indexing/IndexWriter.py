import os
from whoosh import index
from whoosh.fields import Schema, TEXT
from whoosh.analysis import RegexTokenizer


# Efficiency and memory cost should be paid with extra attention.
class IndexWriter:

    def __init__(self):
        index_dir = "index"
        os.makedirs(index_dir, exist_ok=True)
        schema = Schema(
            game_name=TEXT(stored=True),
            game_desc=TEXT(analyzer=RegexTokenizer(), stored=True),
        )
        
        self.writer = index.create_in(index_dir, schema).writer()

    # This method build index for each document.
    # NT: in your implementation of the index, you should transform your string docno into non-negative integer docids,
    # and in MyIndexReader, you should be able to request the integer docid for each docno.
    def index(self, game_name, game_desc):
        self.writer.add_document(game_name = game_name, game_desc = game_desc)

    # Close the index writer, and you should output all the buffered content (if any).
    def close(self):
        self.writer.commit()
