import webbrowser


# A class that stores information about movies.
class Movie():
        """This class provides a way to store movie related information.
        including movie title, box art, and the movie trailer"""
        def __init__(self, movie_title,
                     poster_image, trailer_youtube):
                        """Initialises the Movie Class instance inputs
                        title, image url, youtube video url
                        """

                        self.title = movie_title
                        self.poster_image_url = poster_image
                        self.trailer_youtube_url = trailer_youtube

        def show_trailer(self):
            """opens youtube url to play the trailer via the webbrowser"""
            webbrowser.open(self.trailer_youtube_url)
