#!/usr/bin/env python3

import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class AppWindow(Gtk.ApplicationWindow):
	"""AppWindow class"""
	def __init__(self, *args, **kwargs):
		super(AppWindow, self).__init__(*args, **kwargs)


class Application(Gtk.Application):
	"""Application class"""
	def __init__(self, *args, **kwargs):
		super(Application, self).__init__(
			*args,
			application_id="org.example.myapp",
			**kwargs)
		self.window = None

	def do_activate(self):
		if not self.window:
			self.window = AppWindow(application=self, title="Main Window")
		self.window.present()


if __name__ == '__main__':
	app = Application()
	app.run(sys.argv)