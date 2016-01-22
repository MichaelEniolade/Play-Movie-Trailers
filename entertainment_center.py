import fresh_tomatoes
import media

# movie_name = media.Movie invokes the functions in media.py and defines each movies

# Lucy
lucy = media.Movie("Lucy",
                    """In the opening shot, we see a cell split up into multiple other cells.
                       Then we see a proto-human in prehistoric times drinking from a lake.""",
                     "https://upload.wikimedia.org/wikipedia/en/1/14/Lucy_(2014_film)_poster.jpg",
                     "https://www.youtube.com/watch?v=viJsYmYOZgY",
                     "July 24, 2015",
                     "Luc Besson",
                     "Scarlett Johansson, Morgan Freeman, Min-sik Choi"
                    )

# Lord of the ring
lord_of_the_ring = media.Movie("Lord of the ring",
			       """It seems that the Ring originally belonged to Sauron, the Dark Lord.
			          Sauron wants the Ring back so that he can conquer the world.""",
			       "http://www.darkcarnival.co.za/wp-content/uploads/2015/11/lord-of-the-rings-two-towers-11.jpg",
			       "https://www.youtube.com/watch?v=-JNVtorI3vw",
			       "December 10, 2001",          
			       "Peter Jackson",
			       "Viggo Mortensen, Sean Astin, Cate Blanchett"
                              )

# Star Trek
star_trek = media.Movie("Star Trek",
                        """In the year 2233 a Federation starship, USS Kelvin, investigates a "lightning storm"
                           in space, which the crew soon realizes is a black hole...""",
                        "http://www.monstersandcritics.com/wp-content/uploads/2015/11/star_trek_the_original_series_by_1darthvader-d6ecswd.jpg",
                        "https://www.youtube.com/watch?v=SL37UPUcEd0",
                        "April 6, 2009",
                        "J.J. Abrams",
                        "Roberto Orci, Alex Kurtzman"
                        )

# Transcendence
transcendence = media.Movie("Transcendence",
			    """Dr. Will Caster (Johnny Depp) is the foremost researcher in the field of Artificial Intelligence,
			        working to create a sentient machine that combines the collective intelligence of everything ever known with the full range of human emotions.""",
			    "http://i.jeded.com/i/transcendence.29748.jpg",
			    "https://www.youtube.com/watch?v=QheoYw1BKJ4",
			    "April 10, 2014",
			    "Wally Pfister",
			    "Rebecca Hall, Morgan Freeman, Cillian Murphy"
                          )

# Men in black
men_in_black = media.Movie("Men in black",
                           """The Men in Black are a secret law-enforcement agency
                              that is responsible for policing the extraterrestrial life hidden on Earth...""",
                           "http://www.sonypictures.com/movies/meninblack3/assets/images/onesheet.jpg",
                           "https://www.youtube.com/watch?v=aoyV49FfjOU",
                           "July 2, 1997",
                           "Barry Sonnenfeld",
                           "Lee Jones, K. Jemaine Clement"
                           )

# Mission impossible
mission_impossible = media.Movie("Mission impossible",
			         """Ethan Hunt (Tom Cruise) is an agent and "point man"
			            of an Impossible Missions Force (IMF) team, an unofficial branch of the CIA""",
				 "https://i.ytimg.com/vi/bsEYtBGS6ho/maxresdefault.jpg",
				 "https://www.youtube.com/watch?v=qbg99ykA2bk",
				 "July 27, 2015",
				 "Brian De Palma",
				 "Ving Rhames, Kristin Scott Thomas"                          
                                )

# Build website
movies = [lucy, lord_of_the_ring, star_trek,
          transcendence, men_in_black, mission_impossible]

fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.__module__)
