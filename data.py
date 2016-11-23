import flask, flask.views
import os
import utils

class Data(flask.views.MethodView):
    @utils.login_required
    def get(self):
        
		
		
        return flask.render_template("data.html",)