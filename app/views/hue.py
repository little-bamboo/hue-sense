from flask import render_template, jsonify
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, BaseView, AppBuilder, expose, has_access
from app import appbuilder, db

from app.controllers.soundcapture import SoundCapture
import threading

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""


class Hue(BaseView):
    route_Base = "/hue"

    def __init__(self):
        self._sc = SoundCapture()
        BaseView.__init__(self)

        # Add threading object

    def run_soundcapture(self):
        while True:
            try:
                self._sc.comp.hue.light_state(True)
                self._sc.hue_speech_detection()

            # TODO: Build out other exception handlers
            except KeyboardInterrupt:
                print("KeyboardInterrupt called")
                exit()
            except IOError, e:
                print("Exception: {0}".format(e))
                exit()
            except Exception, e:
                print("Exception: {0}".format(e))
            finally:
                self._sc.comp.hue.light_state(False)
                print("Finally...")

    @expose('/_toggle_soundcapture/<string:state>')
    def toggle_soundcapture(self, state):

        if state == 'Off':
            sound_thread = threading.Thread(target=self.run_soundcapture, name='sound_capture_thread')
            sound_thread.setDaemon(True)
            sound_thread.start()

            state = 'On'

        else:
            # self.sound_process.terminate()
            print "terminate soundcapture"
            # TODO: Terminate thread based on thread name...?

            state = 'Off'

        print(state)
        return jsonify(state)

    @expose('/_toggle_lights/<string:state>')
    def toggle_lights(self, state):

        if state == 'Off':
            self._sc.comp.hue.light_state(True)
            state = 'On'
        else:
            self._sc.comp.hue.light_state(False)
            state = 'Off'

        return jsonify(state)

    @expose('/')
    # @has_access
    def default(self):
        return self.render_template('hue.html')


appbuilder.add_view(Hue, "Hue", href='/hue', category='Hue')
