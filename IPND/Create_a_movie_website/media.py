import webbrowser
#Parent class created to use the repeated variables
class Video():
    def __init__(self,title,post_img,trail_link ):
        self.title = title
        self.poster_image_url = post_img
        self.trailer_youtube_url = trail_link
    def play_trailer(self):
        """This Method executes the trailer of the Movie"""
        webbrowser.open(self.trailer_youtube_url)

class Movie(Video):
    """ This class is used to play trailer for multiple movies"""
    #Parent class variables will be inherited
    def __init__(self,movie_title,post_img,trail_link,movie_duration):
        Video.__init__(self,movie_title,post_img,trail_link)
        self.movie_duration = str(movie_duration)

class Series(Video):
    """This class is used to play trailer for multiple series"""
    #Parent class variables will be inherited
    def __init__(self,series_title,post_img,trail_link, number_of_episode):
        Video.__init__(self,series_title,post_img,trail_link)
        self.number_of_episode = str(number_of_episode)
