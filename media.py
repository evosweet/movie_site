""" This is the mail module of the Movie class """
import webbrowser

class Movie(object):
    """ this class provides a way to store movie related information """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """ uses webbrowser class to open a url"""
        webbrowser.open(self.trailer_youtube_url)
