# import media class
import media

# import fresh_tomatoes class
import fresh_tomatoes

# List of movie dictionaries, each dictionary holds data ( class arguments) for a movie on the page
# URL shortener used to help make code more readable
DEF_MOVIES = [
    {
        "name":"Rouge One",
        "title":"""the story of how the rebels get the plans for the death star""",
        "image_url":"http://tinyurl.com/hegpgtz",
        "video_url":"https://www.youtube.com/watch?v=eUmcneReow8"
    },
    {
        "name":"New Hope",
        "title":"""Led by Princess Leia (Fisher),and its attempt
                to destroy the Galactic Empire's space station, the Death Star""",
        "image_url":"http://tinyurl.com/jml6smh",
        "video_url":"https://www.youtube.com/watch?v=nywPf1p-BBY"
    },
    {
        "name":"Return of the Jedi",
        "title":""" The Galactic Empire, under the direction of the ruthless Emperor,
                is constructing a second Death Star in order to 
                crush the Rebel Alliance once and for all""",
        "image_url": "https://goo.gl/zDRgrd",
        "video_url": "https://www.youtube.com/watch?v=MYD_xxY5wEI"
    },
    {
        "name":"The Empire Strikes Back",
        "title":"""The Galactic Empire, under the leadership of
                the villainous Darth Vader and the Emperor, is in pursuit of
                Luke Skywalker and the rest of the Rebel Alliance.""",
        "image_url":  "https://goo.gl/8h4sBp",
        "video_url": "https://www.youtube.com/watch?v=xESiohGGP7g"
    },
    {
        "name":"The Phantom menace",
        "title":"""The film is set thirty-two years before the original film,
                and follows Jedi Master Qui-Gon Jinn and his apprentice Obi-Wan Kenobi 
                as they protect Queen Amidala, in hopes of securing a peaceful end to a 
                large-scale interplanetary trade dispute.""",
        "image_url": "https://goo.gl/CjZsKt",
        "video_url": "https://www.youtube.com/watch?v=bD7bpG-zDJQ"
    },
    {
        "name":"Attack of the clones",
        "title":""" The Jedi Knights are spread across the galaxy,
        leading a massive war against the Separatists""",
        "image_url":"https://goo.gl/X5WsmI",
        "video_url":"https://www.youtube.com/watch?v=5UnjrG_N8hU"
    }
]

#movie class instance block
ROUGE_ONE = media.Movie(DEF_MOVIES[0]['name'], DEF_MOVIES[0]['title'],
                        DEF_MOVIES[0]['image_url'], DEF_MOVIES[0]['video_url'])

NEW_HOPE = media.Movie(DEF_MOVIES[1]['name'], DEF_MOVIES[1]['title'],
                       DEF_MOVIES[1]['image_url'], DEF_MOVIES[1]['video_url'])

RETURN_OF_THE_JEDI = media.Movie(DEF_MOVIES[2]['name'], DEF_MOVIES[2]['title'],
                                 DEF_MOVIES[2]['image_url'], DEF_MOVIES[2]['video_url'])

EMPIRE_STRIKES_BACK = media.Movie(DEF_MOVIES[3]['name'], DEF_MOVIES[3]['title'],
                                  DEF_MOVIES[3]['image_url'], DEF_MOVIES[3]['video_url'])

THE_PHANTOM_MENACE = media.Movie(DEF_MOVIES[4]['name'], DEF_MOVIES[4]['title'],
                                 DEF_MOVIES[4]['image_url'], DEF_MOVIES[4]['video_url'])

ATTACK_OF_THE_CLONES = media.Movie(DEF_MOVIES[5]['name'], DEF_MOVIES[5]['title'],
                                   DEF_MOVIES[5]['image_url'], DEF_MOVIES[5]['video_url'])


# create a list of movie classes to pass to fresh_tomatoes.open_movies_page
LIST_OF_MOVIES = [ROUGE_ONE,
                  NEW_HOPE,
                  RETURN_OF_THE_JEDI,
                  EMPIRE_STRIKES_BACK,
                  THE_PHANTOM_MENACE,
                  ATTACK_OF_THE_CLONES]

# pass the movie class list to fresh_tomatoes and start application
fresh_tomatoes.open_movies_page(LIST_OF_MOVIES)
