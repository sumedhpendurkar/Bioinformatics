from Bio import SeqIO
import gtk
#put everything that is related to graphics in this class
class gtkthings:
	def file_browser(self, widget):
		dialog = gtk.FileChooserDialog("Open",
        	                       None,
        	                       gtk.FILE_CHOOSER_ACTION_OPEN,
        	                       (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
        	                        gtk.STOCK_OPEN, gtk.RESPONSE_OK))
		dialog.set_default_response(gtk.RESPONSE_OK)
		filter = gtk.FileFilter()
		filter.set_name("All files")
		filter.add_pattern("*")
		dialog.add_filter(filter)
		filter = gtk.FileFilter()
		filter.set_name("Images")
		filter.add_mime_type("image/png")
		filter.add_mime_type("image/jpeg")
		filter.add_mime_type("image/gif")
		filter.add_pattern("*.png")
		filter.add_pattern("*.jpg")
		filter.add_pattern("*.gif")
		filter.add_pattern("*.tif")
		filter.add_pattern("*.xpm")
		dialog.add_filter(filter)
		response = dialog.run()
		if response == gtk.RESPONSE_OK:
			self.text.set_text(dialog.get_filename())
		elif response == gtk.RESPONSE_CANCEL:
			self.text.set_text("--No files selected--")
		dialog.destroy()

	def delete_event(self, widget, event, data=None):
		gtk.main_quit()
		return False
	def dna_process(self, widget):
		if(self.text.get_text()):
			stri = ''
			self.label.set_text(self.text.get_text())
			for index, record in enumerate(SeqIO.parse(self.text.get_text(), "genbank")):
				stri = stri + str("index %i, ID = %s, length %i, with %i features"
		%(index, record.id, len(record.seq), len(record.features)))
				stri = stri + str(record)
				stri = stri + ("\n")
			dir(record)
			record.seq
		else:
			self.label.set_text("--No file selected--")
		self.label.set_text(stri)
	def __init__(self):
		self.main_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		#some stuff to make it look pretty
		self.main_window.set_default_size(500, 550)
		self.main_window.set_title("DNA matching")
		#please do this to ensure the exit button on top of window works
		self.main_window.connect("delete_event", self.delete_event)
		self.main_window.set_border_width(10)
		##creates boxes and packing buttons in it
		#create a vertical box and pack horizontal boxes in it
		vertical_alignment = gtk.VBox(False, 0)
		#just an image
		image_box = gtk.HBox(False, 0)
		image = gtk.Image()
		image.set_from_file("./dna.jpeg")
		image_box.pack_start(image, True, False, 0)
		vertical_alignment.pack_start(image_box, False, False, 2)
		image_box.show()
		image.show()
		#a box for open
		openbox = gtk.HBox(False, 0)
		self.text = gtk.Entry()
		openbox.pack_start(self.text, True, True, 0)
		button = gtk.Button("Open a file for testing")
		button.connect("clicked", self.file_browser)
		self.text.set_text("--No File Selected--")
		openbox.pack_start(button, False, False, 0)
		vertical_alignment.pack_start(openbox, False, False, 2)
		self.text.show()
		button.show()
		#output thing
		outputbox = gtk.HBox(False, 0)
		frame = gtk.Frame("Output")
		self.label = gtk.Label("----Please Select a File----")
		self.label.set_line_wrap(True)
	        frame.add(self.label)
		vertical_alignment.pack_start(frame, False, False, 2)
		#a box of quit and process
		lastbox = gtk.HBox(False, 0)
		process_button = gtk.Button("Process DNA")
		process_button.connect("clicked", self.dna_process)
		quit_button = gtk.Button("Quit", gtk.STOCK_QUIT)
		quit_button.connect("clicked", gtk.main_quit)
		lastbox.pack_start(process_button, True, False, 0)
		lastbox.pack_start(quit_button, True, False, 0)
		vertical_alignment.pack_end(lastbox, False, False, 0)
		process_button.show()
		quit_button.show()
		#add vertical box to the window
		self.main_window.add(vertical_alignment)
		#last step to be done so that everything is visible at once
		openbox.show()
		frame.show()
		self.label.show()
		lastbox.show()
		vertical_alignment.show()
		self.main_window.show()
def main():
	gtk.main()
	return 0
if __name__== "__main__":
	graphics = gtkthings()
	main()
