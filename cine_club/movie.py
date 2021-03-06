from pathlib import Path
import json
import logging


CUR_DIR = Path(__file__).resolve().parent
DATA_FILE = CUR_DIR / "data" / "movies.json"
logging.basicConfig(level=logging.DEBUG,
                    filename=CUR_DIR/"movies.log",
                    filemode="w",
                    format='%(asctime)s - %(levelname)s - %(message)s')

<<<<<<< HEAD
def get_movies():
    with open(DATA_FILE,"r") as f :
        movies_title = json.load(f)
        
    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies
    
class Movie:
    def __init__(self,title:str) -> None:
        self.title = title.title()
=======
class Movie:
    def __init__(self,title:str) -> None:
        self.title = title.title()
        self.remove_from_movies()
        # self.add_to_movies()
        # self._get_movies()
        # self._write_movies()
>>>>>>> 8c61fcd7d8f40ca7f98d0e33d740c4aa052b8920
        
    def __str__(self):
        return f"{self.title}"
    
    def _get_movies(self):
        with open(DATA_FILE,"r") as f:
            return json.load(f)
            
    def _write_movies(self, movies):
        with open(DATA_FILE, "w") as f:
            json.dump(movies,f,indent=4)
            
    def add_to_movies(self):
<<<<<<< HEAD
        movies = self._get_movies()
        if self.title in movies:
            logging.warning("Film déjà dans la base")
            return False
=======
        #recup la liste des films
        movies = self._get_movies()
        #check que le film n'est pas déjà dans la liste
        if self.title in movies:
            logging.warning("Film déjà dans la base")
            return False
        #Si ce n'est pas le cas on l'ajoute
>>>>>>> 8c61fcd7d8f40ca7f98d0e33d740c4aa052b8920
        else:
            movies.append(self.title)
            self._write_movies(movies)
            return True
    
    def remove_from_movies(self):
<<<<<<< HEAD
        movies = self._get_movies()
=======
        #recup la liste des films
        movies = self._get_movies()
        #check si le film est dans la liste
>>>>>>> 8c61fcd7d8f40ca7f98d0e33d740c4aa052b8920
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning("Film absent de la liste")
            return False
<<<<<<< HEAD
        
if __name__ == "__main__":
    m = Movie("peter pan")
    print(m._get_movies())
    print(get_movies())
=======
        #si c'est le cas enlever le film de la liste
        
if __name__ == "__main__":
    m = Movie("peter pan")
    print(m._get_movies())
>>>>>>> 8c61fcd7d8f40ca7f98d0e33d740c4aa052b8920
