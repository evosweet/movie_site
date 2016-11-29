""" This is the main module for the Movie class """
# import webbrowser class to use open function
import webbrowser

class Movie(object):
    """ this class provides a way to store movie related information """
    # constant list of movie ratings
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        """ initiate class arguments make then available to the class with the self keyword """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """ uses webbrowser class to open a url"""
        webbrowser.open(self.trailer_youtube_url)
