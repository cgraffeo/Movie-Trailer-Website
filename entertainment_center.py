# -*- coding: utf-8 -*-
# Import dependencies
import media
import fresh_tomatoes

# One instance created per movie with individual attributes
the_martian = media.Movie("The Martian",
                        "Matt Damon gets stranded on Mars. Can he be rescued?",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcTkKPZ7EIOafEsemyn6zTIDeGYthKC_Okgxi1eX6diuOT3xKWXQ",  # NOQA
                        "https://www.youtube.com/watch?v=ej3ioOneTy8")

law_abiding_citizen = media.Movie("Law Abiding Citizen",
                     "A Man is pushed beyond his breaking point when his "
                     "family is brutally murdered",
                     "https://upload.wikimedia.org/wikipedia/en/9/95/Law_abiding_citizen_ver5.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=LX6kVRsdXW4")

deadpool = media.Movie("Deadpool",
                     "A former special ops soldier gets into some big "
                     "trouble.",
                     "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=ONHBaC-pfsk")

limitless = media.Movie("Limitless",
                     "A man finds a new drug that increases intelligence",
                     "https://upload.wikimedia.org/wikipedia/en/1/17/Limitless_Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=jOLqNOfzus4")

fury = media.Movie("Fury",
                "A WWII Sherman tank crew gets into some big trouble",
                "https://upload.wikimedia.org/wikipedia/en/1/17/Fury_2014_poster.jpg",  # NOQA
                "https://www.youtube.com/watch?v=-OGvZoIrXpg")

intersteller = media.Movie("Intersteller",
                        "A crew tries to save the population of Earth",
                        "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=2LqzF5WauAw")

# Movies array for use with fresh_tomatoes
movies = [the_martian, law_abiding_citizen, deadpool, limitless, fury,
          intersteller]
# Opens fresh_tomatoes page
fresh_tomatoes.open_movies_page(movies)
