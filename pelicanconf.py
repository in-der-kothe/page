AUTHOR = 'Marc Gorzala'
SITENAME = 'Kultur in der Kothe'
SITEURL = "https://kultur.in-der-kothe.de"

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'de'



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Dancier", "https://project.dancier.net"),
)

# Social widget
SOCIAL = (
#    ("You can add links in your config file", "#"),
#    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

import os

# Dynamically add all subdirectories in content to STATIC_PATHS
STATIC_PATHS = ["images"] + [d for d in os.listdir("content") if os.path.isdir(os.path.join("content", d))]

# Automatically copy static files from article folders (e.g., images in content/foo/)
ARTICLE_STATIC_CREATORS = True
