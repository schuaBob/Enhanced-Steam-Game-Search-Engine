import os
from whoosh import index
from whoosh.fields import Schema, TEXT, KEYWORD
from whoosh.analysis import RegexTokenizer


class IndexWriter:
    def __init__(self):
        index_dir = "index"
        if os.path.exists(index_dir):
            os.system("rm -rf index")
        os.makedirs(index_dir)
        schema = Schema(
            game_name=TEXT(stored=True),
            game_desc=TEXT(analyzer=RegexTokenizer(), stored=True),
            tags=KEYWORD(stored=True),
        )

        self.writer = index.create_in(index_dir, schema).writer()

    def index(self, game_name, game_desc, tags: list):
        self.writer.add_document(
            game_name=game_name,
            game_desc=game_desc,
            tags=" ".join([w.lower() for w in tags]),
        )

    def close(self):
        self.writer.commit()
