import webbrowser

# class Movie defines what a movie should include


class Movie():
    """
    The class Movie defines what a movie should include.
    The __init__ function initializes a new instance of the class Movie.
    A new instance of the class Movie should include the movie's title,
    storyline, poster image, youtube trailer, release date, director,
    and actors.
    """
    
    """This class provides a way to store movie related information"""
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image_url,
                 trailer_youtube_url, release_date, director, actors):
        self.title = movie_title
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.release_date = release_date
        self.director = director
        self.actors = actors

    '''
    method show_trailer opens a new web browser window containing the
    movie's trailer
    '''

    def show_trailer(self):
        webbrowser.open(self.trailer)
