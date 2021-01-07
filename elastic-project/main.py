from elasticsearch import Elasticsearch
import json
from data_structures import Movie


class ElasticLoader():
    def __init__(self):
        print("hello world")

        self.es = self.init_elastic()

        self.filename = "movies-small.csv"
        self.file_loc = "c:/Elastic/ml-latest-small/"
        

        self.process_file()

    def init_elastic(self):
        
        return Elasticsearch([{'host':'localhost','port':9200}])


    def process_file(self):

        first = True
        movie = None
        with open(self.file_loc + self.filename) as file_ref:
            for line in file_ref:
                
                if not first:
                    movie = Movie(line)    
                    #print(movie.format_json()) 
                    self.insert(movie) 
                first = False    
    

    def insert(self,movie:Movie):

        res = self.es.index(index='movies',doc_type='movie',id=movie.id,body=movie.format_json())
        print(res)


if __name__ == "__main__":
    runner = ElasticLoader()



