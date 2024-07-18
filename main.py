import os
import time
import webbrowser

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.core.clipboard import Clipboard

from filesharer import FileSharer

# Load the Kivy language file
Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        """
        Starts the camera and updates the button text.
        """
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera_button.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        """
        Stops the camera and updates the button text.
        """
        self.ids.camera.opacity = 0
        self.ids.camera.play = False
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        """
        Captures an image with the current time as the filename and saves it.
        """
        try:
            Logger.info("Current working directory: %s", os.getcwd())
            os.makedirs('files', exist_ok=True)  # Create files/ folder if it doesn't exist
        except OSError as ose:
            Logger.error("Error creating directory: %s", ose)
            return

        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = f'files/{current_time}.png'
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath
        Logger.info('Captured image saved at: %s', self.filepath)


class ImageScreen(Screen):
    link_message = 'Create a link first!'

    def create_link(self):
        """
        Uploads the captured image to the web and displays the generated link.
        """
        try:
            filepath = App.get_running_app().root.ids.camera_screen.filepath
            fileshare = FileSharer(filepath)
            self.url = fileshare.share()
            self.ids.link.text = self.url
            Logger.info('Shared URL: %s', self.url)
        except Exception as e:
            Logger.error("Error creating link: %s", e)
            self.ids.link.text = 'Error creating link'

    def copy_link(self):
        """
        Copies the generated link to the clipboard.
        """
        if hasattr(self, 'url'):
            Clipboard.copy(self.url)
        else:
            self.ids.link.text = self.link_message

    def open_link(self):
        """
        Opens the generated link in the default web browser.
        """
        if hasattr(self, 'url'):
            webbrowser.open(self.url)
        else:
            self.ids.link.text = self.link_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
