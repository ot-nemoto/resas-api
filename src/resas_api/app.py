# -*- coding: utf-8 -*-

import connexion
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'handlers': {
        'consoleHandler': {
            'class': 'logging.StreamHandler',
            'formatter': 'consoleFormatter',
            'stream': 'ext://sys.stdout'
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['consoleHandler']
    },
    'formatters': {
        'consoleFormatter': {
            'format': '[%(levelname)-5s] - %(message)s'
        },
    }
})

options = {"swagger_ui": True}
app = connexion.FlaskApp(__name__, specification_dir='.', options=options)
app.add_api('openapi.yaml')
app.app.config['JSON_AS_ASCII'] = False
app.app.config['JSON_SORT_KEYS'] = False

if __name__ == "__main__":
    app.run(port=8080)
