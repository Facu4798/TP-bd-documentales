def mdb_connect():
    from pymongo import MongoClient
    import os
    from dotenv import load_dotenv

    load_dotenv(dotenv_path="./src/python/functions/mongodb/creds.env")

    CONN_STR = os.getenv("CONN_STR")
    client = MongoClient(CONN_STR)
    return client