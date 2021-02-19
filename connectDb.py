import config

def connectSessionMongo():
    if config.DB_USERNAME and config.DB_PASSWORD:
        uriStr = "mongodb://%s:%s@%s/%s"
        uri = uriStr % (config.DB_USERNAME, config.DB_PASSWORD, config.DB_ENDPOINT, config.DB_NAME)
    else:
        uriStr = "mongodb://%s/%s"
        uri = uriStr % (config.DB_ENDPOINT, config.DB_NAME)
    sdb = MongoClient(uri,serverSelectionTimeoutMS=config.DB_TO)
    return sdb[config.DB_NAME]
