from pathlib import Path
import json
import logging


CUR_DIR = Path(__file__).resolve().parent
DATA_FILE = CUR_DIR / "data" / "movies.json"
logging.basicConfig(level=logging.DEBUG,
                    filename=CUR_DIR/"movies.log",
                    filemode="w",
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_movies():
    with open(DATA_FILE,"r") as f :
        movies_title = json.load(f)
        
    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies
    
class Movie:
    def __init__(self,title:str) -> None:
        self.title = title.title()
        
    def __str__(self):
        return f"{self.title}"
    
    def _get_movies(self):
        with open(DATA_FILE,"r") as f:
            return json.load(f)
            
    def _write_movies(self, movies):
        with open(DATA_FILE, "w") as f:
            json.dump(movies,f,indent=4)
            
    def add_to_movies(self):
        movies = self._get_movies()
        if self.title in movies:
            logging.warning("Film déjà dans la base")
            return False
        else:
            movies.append(self.title)
            self._write_movies(movies)
            return True
    
    def remove_from_movies(self):
        movies = self._get_movies()
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning("Film absent de la liste")
            return False
        
if __name__ == "__main__":
    m = Movie("peter pan")
    print(m._get_movies())
    print(get_movies())