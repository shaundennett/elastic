from elasticsearch import Elasticsearch


class ElasticLoader():

    def __init__(self):

        print("hello world")
        es=Elasticsearch(['http://127.0.0.1:9200/'])
        print("Done!")

        print("Count number of users...")
        print(es.count(index='movies'))
            

if __name__ == "__main__":
    runner = ElasticLoader()



