import json
class Movie():

    def __init__(self , raw_data):
           
        self.id = ""
        self.title = ""
        self.year = ""
        self.genre = []
        
        
        self.data_extracted = []
        self.parse_file(raw_data)
        


    def parse_file(self, data):

        for item in data.split(','):
            self.data_extracted.append(item)

        self.id = self.data_extracted[0]
        
        self.title = self.data_extracted[1][:len(self.data_extracted[1]) - 7]
        self.year = self.data_extracted[1][len(self.data_extracted[1]) - 5: len(self.data_extracted[1]) -1]
        for genre_item in self.data_extracted[2].split('|'):
            self.genre.append(genre_item.strip('\n'))
    
    def format_json(self):
        
        return {
            "id":self.id,
            "title":self.title,
            "year":self.year,
            "genre":self.genre
        }

    def pretty_print(self):

        print("---------------------------")
        print(self.id)
        print(self.title)
        print(self.year)
        print(self.genre)
        print("---------------------------")
        
if __name__ == "__main__":
    
    dataIn = "1376,Star Trek IV: The Voyage Home (1986),Adventure|Comedy|Sci-Fi"
    data = Movie(dataIn)
    data.pretty_print()