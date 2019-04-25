#/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gio, Gtk

class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, appplication_id="org.example.myapp",
        flags=Gio.ApplicationFlags.HANDLE_COMMAND_LINE,
        **kwargs)
        self.window = None
        self.add_main_option("test", ord("t"), GLib.OptionFlags.NONE, GLib.OptionArg.NONE,
        "Command line test", None)

        def do_startup(self):
            Gtk.Application.do_startup(self)
            action = Gio.SimpleAction.new("quit", None)
            action.connect("activate", self.on_quit)
            self.add_action(action)