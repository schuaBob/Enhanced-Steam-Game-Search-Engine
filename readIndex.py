from indexing.IndexReader import MyIndexReader
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("parser_type", default="single")
    parser.add_argument("query", default="")
    args = parser.parse_args()
    # can be "single" or "multi"
    indexReader = MyIndexReader(args.parser_type)
    result = indexReader.search(args.query)

    for res in result:
        print(f"name: {res['game_name']}, score:{res.score}")