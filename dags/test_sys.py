import os
import sys

sys.path.insert(0, os.path.abspath("."))

for path in sys.path:
    print(path)


def test():
    from extraction.mongo_extraction import mongo_connection
    from extraction.utils.write_s3 import write_s3


test()
