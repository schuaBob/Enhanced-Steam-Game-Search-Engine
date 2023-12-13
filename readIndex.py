from indexing.IndexReader import MyIndexReader
import argparse
if __name__ == "__main__":
    indexReader = MyIndexReader()
    parser = argparse.ArgumentParser()
    parser.add_argument("query", default="")
    args = parser.parse_args()
    indexReader.search(args.query)