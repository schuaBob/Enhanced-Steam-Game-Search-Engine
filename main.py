from indexing.IndexWriter import IndexWriter
import json
from tqdm import tqdm


if __name__ == "__main__":
    indexWriter = IndexWriter()
    data_file = "data/cleaned_steam.json"
    with open(data_file) as f:
        data = json.load(f)
    for game in tqdm(data):
        indexWriter.index(game_name=game["name"], game_desc=game["desc"])
    indexWriter.close()
    print("Indexing done")
