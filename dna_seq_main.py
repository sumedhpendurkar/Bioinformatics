from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_rna, generic_protein
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
		filter.set_name("Genbank")
		filter.add_pattern("*.gbk")
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
		if(self.text.get_text() == None):
			self.label.set_text("No file selected")
		else:
			try:
				seq = SeqIO.parse(self.text.get_text(), "genbank")
				counts = []
				#for index, record in enumerate(seq):
					#cnt = record.count(#herre is the dna to be matched))
					#if len(counts) < 5 or cnt > min(counts):
					#	counts.append(min.counts)
				self.label.set_text(string)
			#write code here
			except:
				self.label.set_text("Invalid file")
	def sample_calcu(widget, self, dna_seq, l1, l2, l3, l4, l5):
		l1.set_text("Complement : " + str(Seq(dna_seq.get_text(), generic_dna).complement()))
		l2.set_text("Reverse Complement : " + str(Seq(dna_seq.get_text(), generic_dna).reverse_complement()))
		l3.set_text("Transcription : " + str(Seq(dna_seq.get_text(), generic_dna).transcribe()))
		l4.set_text("Reverse Transcription : " + str(Seq(dna_seq.get_text(), generic_rna).back_transcribe()))
		l5.set_text("Translation : " + str(Seq(dna_seq.get_text(), generic_dna).translate(stop_symbol = " | ")))
	def page2(self):
		vertical_alignment = gtk.VBox(False, 0)
		dna_seq_box = gtk.HBox(False, 0)
		dna_seq = gtk.Entry()
		dna_seq_box.pack_start(dna_seq, True, True, 4)
		vertical_alignment.pack_start(dna_seq_box, False, False, 0)
		dna_seq_box.show()
		dna_seq.show()
		dna_seq_box = gtk.HBox(False, 0)
		outputbox = gtk.HBox()
		label =	gtk.Label()
		txt = "Features of DNA : "
		label.set_text(txt)
		outputbox.pack_start(label, False, False, 0)
		label.show()
		outputbox1 = gtk.HBox()
		label1 = gtk.Label()
		label1.show()
		outputbox1.pack_start(label1, False, False, 0)
		outputbox2 = gtk.HBox(False, 0)
		label2 = gtk.Label()
		label2.show()
		outputbox2.pack_start(label2, False, False, 0)
		outputbox3 = gtk.HBox(False, 0)
		label3 = gtk.Label()
		label3.show()
		outputbox3.pack_start(label3, False, False, 0)
		outputbox4 = gtk.HBox(False, 0)
		label4 = gtk.Label()
		label4.show()
		outputbox4.pack_start(label4, False, False, 0)
		outputbox5 = gtk.HBox(False, 0)
		label5 = gtk.Label()
		label5.show()
		outputbox5.pack_start(label5, False, False, 0)
		outputbox.show()
		outputbox1.show()
		outputbox2.show()
		outputbox3.show()
		outputbox4.show()
		outputbox5.show()
		vertical_alignment.pack_start(outputbox, False, False, 10)
		vertical_alignment.pack_start(outputbox1, False, False, 10)
		vertical_alignment.pack_start(outputbox2, False, False, 10)
		vertical_alignment.pack_start(outputbox3, False, False, 10)
		vertical_alignment.pack_start(outputbox4, False, False, 10)
		vertical_alignment.pack_start(outputbox5, False, False, 10)
		vertical_alignment.pack_start(dna_seq_box, False, False,10)
		dna_seq_box.show()
		lastbox = gtk.HBox(False, 0)
		process_button = gtk.Button("Process DNA")
		process_button.connect("clicked", self.sample_calcu, dna_seq, label1, label2, label3, label4, label5)
		quit_button = gtk.Button("Quit", gtk.STOCK_QUIT)
		quit_button.connect("clicked", gtk.main_quit)
		lastbox.pack_start(process_button, True, False, 0)
		lastbox.pack_start(quit_button, True, False, 0)
		vertical_alignment.pack_end(lastbox, False, False, 0)
		process_button.show()
		quit_button.show()
		lastbox.show()
		vertical_alignment.show()
		return vertical_alignment
	def __init__(self):
		self.main_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		nbk = gtk.Notebook()
		nbk.show()
		#some stuff to make it look pretty
		self.main_window.set_default_size(700, 750)
		self.main_window.set_title("DNA sequence analyzer")
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
		#a label for input boxes
		input_label = gtk.Label("Select the genbank of the suspects")
		vertical_alignment.pack_start(input_label, False, False, 5)
		#a box for open
		input_label.show()
		openbox = gtk.HBox(False, 0)
		self.text = gtk.Entry()
		openbox.pack_start(self.text, True, True, 5)
		button = gtk.Button("Open..")
		button.connect("clicked", self.file_browser)
		self.text.set_text("--No File Selected--")
		openbox.pack_start(button, False, False, 0)
		vertical_alignment.pack_start(openbox, False, False, 10)
		self.text.show()
		button.show()
		#sequence input
		seq_box = gtk.HBox(False, 0)
		self.seq_text = gtk.Entry()
		seq_box.pack_start(self.seq_text, True, True, 5)
		vertical_alignment.pack_start(seq_box, False, False, 10)
		self.seq_text.show()
		seq_box.show()
		#output thing
		outputbox = gtk.HBox(False, 0)
		frame = gtk.Frame("Output")
		self.label = gtk.Label("----Please Select a File----")
		self.label.set_line_wrap(True)
	        frame.add(self.label)
		vertical_alignment.pack_start(frame, False, False, 5)
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
		nbk.append_page(vertical_alignment, gtk.Label("Crimal Finder"))
		vertical2 = self.page2()
		nbk.append_page(vertical2, gtk.Label("Sample"))
		self.main_window.add(nbk)
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
