from flask import render_template, jsonify
from app import appbuilder
from flask_appbuilder import BaseView, expose



class Help(BaseView):
    route_Base = "/help"

    @expose('/')
    # @has_access
    def default(self):
        return render_template('help.html')


appbuilder.add_view(Help, "Help", href='/help', icon="fa-folder-open-o", category="Help", category_icon='fa-envelope')