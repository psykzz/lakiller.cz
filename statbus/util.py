from flask import request
from playhouse.flask_utils import FlaskDB


class FlaskDBWrapper(FlaskDB):

    def connect_db(self):
        if request.endpoint in ('static',):
            return
        return self.database.connect()
