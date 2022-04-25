from PySide2 import QtWidgets, QtCore
from movie import Movie, get_movies

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()
        
    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.le_movieTitle = QtWidgets.QLineEdit()
        self.lw_movies = QtWidgets.QListWidget()
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_addMovie = QtWidgets.QPushButton("Ajouter un film")
        self.btn_removeMovies = QtWidgets.QPushButton("Supprimer le(s) film(s)")
        
        self.main_layout.addWidget(self.le_movieTitle)
        self.main_layout.addWidget(self.btn_addMovie)
        self.main_layout.addWidget(self.lw_movies)
        self.main_layout.addWidget(self.btn_removeMovies)
    
    def populate_movies(self):
        movies = get_movies()
        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title) #affiche le texte
            lw_item.movie = movie
            # lw_item.setData(QtCore.Qt.UserRole, movie) #attache l'instance Movie à l'item 
            self.lw_movies.addItem(lw_item)
    
    def setup_connections(self):
        self.le_movieTitle.returnPressed.connect(self.add_movie)
        self.btn_addMovie.clicked.connect(self.add_movie) 
        self.btn_removeMovies.clicked.connect(self.remove_movie) 
            
    def add_movie(self):
        #recup le texte dans le line edit
        movie_title = self.le_movieTitle.text()
        if not movie_title:
            return False

        #Créer une instance movie
        movie = Movie(movie_title)
        #Ajouter le film dans le fichier json
        resultat = movie.add_to_movies()
        if resultat:        
        #AJouter le titre dans le list widget
            lw_item = QtWidgets.QListWidgetItem(movie.title) #affiche le texte
            # lw_item.setData(QtCore.Qt.UserRole, movie) #attache l'instance Movie à l'item
            lw_item.movie = movie
            self.lw_movies.addItem(lw_item)
            self.le_movieTitle.setText("")
        self.le_movieTitle.setText("")
        
    def remove_movie(self):
        for selected_item in self.lw_movies.selectedItems():
            movie = selected_item.movie
            # movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.lw_movies.takeItem(self.lw_movies.row(selected_item))
        print("On supprime un film")
            
app = QtWidgets.QApplication([])
window = App()
window.show()
app.exec_()