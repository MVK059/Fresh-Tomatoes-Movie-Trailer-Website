""" Defines the Movie class and describes the contents in it """

import webbrowser

class Movie():
    """
    This class stores all the information about the movie to be displayed on the website

    Args:
        (str) movie_title - title of the movie
        (str) movie_storyline - storyline of the movie
        (str) movie_director -director of the movie
        (str) poster_image - image link for the poster of the movie
        (str) trailer_youtube - youtube link for the trailer of the movie

    Returns:
        none
    """
    def __init__(self, movie_title, movie_storyline, movie_director, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.director = movie_director
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    """
    This method opens the youtube url in a browser
    Args:
        none.
    Returns:
        none.
    """
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)