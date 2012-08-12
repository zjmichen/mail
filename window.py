from gi.repository import Gtk
import Mailctl

class MailWindow():

	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file('main.ui')

		window = builder.get_object('main_window')
		builder.connect_signals({ "on_window_destroy" : Gtk.main_quit })
		window.show()

if (__name__ == "__main__"):
	app = MailWindow()
	Gtk.main()