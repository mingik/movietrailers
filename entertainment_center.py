from media import Movie

def list_of_movies():
  """
  Simple function that returns a list of three Movie instances
  """
  movie_titles = ['Thin Red Line', 'Heat', 'Glengarry Glenn Ross']
  trailer_youtube_urls = ['www.youtube.com/watch?v=LCmlOhsIwBk', 'www.youtube.com/watch?v=0xbBLJ1WGwQ', 'www.youtube.com/watch?v=_VrekKSuFto']
  poster_image_urls = ['http://www.impawards.com/1998/posters/thin_red_line.jpg','http://imgc.allpostersimages.com/images/P-488-488-90/40/4030/T4BLF00Z/posters/heat-spanish-movie-poster-1995.jpg','http://imgc.allpostersimages.com/images/P-473-488-90/56/5666/VH3UG00Z/posters/glengarry-glen-ross.jpg']
  # generate list from created Movie instance from each tuple coming from zipped lists above
  return [Movie(url,title,poster) for (url,title,poster) in zip(trailer_youtube_urls, movie_titles, poster_image_urls)]
    
