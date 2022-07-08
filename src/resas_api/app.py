# -*- coding: utf-8 -*-

import connexion

options = {"swagger_ui": True}
app = connexion.FlaskApp(__name__, specification_dir='openapi/', options=options)
app.add_api('resas_api.yaml')
app.app.config['JSON_AS_ASCII'] = False
app.app.config['JSON_SORT_KEYS'] = False

if __name__ == "__main__":
    app.run(port=8080)
