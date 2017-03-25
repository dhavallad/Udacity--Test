__author__ = "Dhaval Lad"

import webbrowser

class Movie():
    """
    This is class for movie.
    :return:
    """
       
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, year):
        """
        Initianize class variables for movie title, storyline, poster 
        image, Youtube trailer, and year.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = year

    def show_trailer(self):
        """
        This method opens movie trailer URL.
        """
        webbrowser.open(self.trailer_youtube_url)
