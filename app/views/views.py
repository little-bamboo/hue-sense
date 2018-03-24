from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, BaseView, AppBuilder, expose, has_access
from app import appbuilder, db

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""


class Hue(BaseView):
    route_Base = "/hue"

    @expose('/method1/<string:param1>')
    def method1(self, param1):
        # do something with param1
        # and return it
        return param1

    @expose('/method2/<string:param2>')
    def method2(self, param2):
        # do something with param2
        return param2

    @expose('/')
    @has_access
    def default(self):
        return self.render_template('hue.html')


appbuilder.add_view(Hue, "Hue", href='/hue', category='Hue')


class Help(BaseView):
    route_Base = "/help"

    @expose('/')
    @has_access
    def default(self):
        return render_template('help.html')


appbuilder.add_view(Help, "Help", href='/help', icon="fa-folder-open-o", category="Help", category_icon='fa-envelope')

# """
#     Application wide 404 error handler
# """
#
# @appbuilder.app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404
#
#
# db.create_all()
