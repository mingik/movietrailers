class Movie():
  """
  A simple class that represents a movie based on
  provided youtube url, title and poster url.
  """
  def __init__(self,trailer_youtube_url, title, poster_image_url):
    self.trailer_youtube_url = trailer_youtube_url
    self.title = title
    self.poster_image_url = poster_image_url
