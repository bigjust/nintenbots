import os

NICK = os.environ.get('HELGA_NICK', 'aineko')

SERVER = {
    'HOST': os.environ.get('HELGA_IRC_SERVER'),
    'PORT': 6667,
    'SSL': False,
}

CHANNELS = [
    (os.environ.get('HELGA_IRC_CHANNEL', '#helga-dev'),)
]

DATABASE = {
    'HOST': os.environ.get('HELGA_MONGO_HOST'),
    'PORT': 27017,
    'DB': os.environ.get('HELGA_MONGO_DB', 'helga')
}
