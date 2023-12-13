from indexing.IndexReader import MyIndexReader
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("parser_type", default="single")
    parser.add_argument("query", default="")
    args = parser.parse_args()
    # can be "single" or "multi"
    indexReader = MyIndexReader(args.parser_type)
    indexReader.search(args.query)