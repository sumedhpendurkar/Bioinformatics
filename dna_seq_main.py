from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_rna, generic_protein
import gtk
def kmp(pat, txt):
	M = len(pat)
	N = len(txt)
	lps = [0]*M
	j = 0
	matches = 0
	computeLPSArray(pat, M, lps)
	i = 0
	while i < N:
		if pat[j] == txt[i]:
			i += 1
			j += 1
 
		if j == M:
			matches+=1
			j = lps[j-1]
 
		elif i < N and pat[j] != txt[i]:
			if j != 0:
				j = lps[j-1]
			else:
				i += 1
	return matches
def computeLPSArray(pat, M, lps):
	len = 0
 
	lps[0]
	i = 1
 
	while i < M:
		if pat[i]==pat[len]:
			len += 1
            		lps[i] = len
			i += 1
		else:
			if len != 0:
				len = lps[len-1]
 
			else:
				lps[i] = 0
				i += 1

#
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
			seq = SeqIO.parse(self.text.get_text(), "genbank")
			counts_max = 0
			counts_index = 0
			for index, record in enumerate(seq):
				cnt = kmp(self.seq_text.get_text().upper(),str(record.seq))
				if (counts_max < cnt):
					counts_max = cnt
					counts_index = index
			if counts_max != 0:
				self.label.set_text("Most Probable suspect has index %d " %(counts_index) + " no of matches : %d " %(counts_max))
			else:
				self.label.set_text("No match found, find other suspects")
	def sample_calcu(widget, self, dna_seq, l):
		tmp = dna_seq.get_text()
		gn = tmp.count("G")
		an = tmp.count("A")
		cn = tmp.count("C")
		tn = tmp.count("T")
		total = an + gn + cn + tn
		l[1].set_text("Complement : " + str(Seq(dna_seq.get_text(), generic_dna).complement()))
		l[2].set_text("Reverse Complement : " + str(Seq(dna_seq.get_text(), generic_dna).reverse_complement()))
		l[3].set_text("Transcription : " + str(Seq(dna_seq.get_text(), generic_dna).transcribe()))
		l[4].set_text("Reverse Transcription : " + str(Seq(dna_seq.get_text(), generic_rna).back_transcribe()))
		l[5].set_text("Translation : " + str(Seq(dna_seq.get_text(), generic_dna).translate(stop_symbol = " | ")))
		l[6].set_text("Melting Temperature : " + str(4 * dna_seq.get_text().count("GC") + 2 * dna_seq.get_text().count('AT')))
		l[7].set_text("GC / AT content : " + str(dna_seq.get_text().count("GC")) + ' / ' + str(dna_seq.get_text().count("AT")))
		l[8].set_text("Molecular Weight : " + str(329.2 * gn + an * 313.2 + 304.2 * tn + 289.2 * cn))
		l[9].set_text("Percentage A : " + str(an*100.0/total))
		l[10].set_text("Percentage T : " + str(tn*100.0/total))
		l[11].set_text("Percentage G : " + str(gn*100.0/total))
		l[12].set_text("Percentage C : " + str(cn*100.0/total))
	def page2(self):
		vertical_alignment = gtk.VBox(False, 0)
		image_box = gtk.HBox(False, 0)
		image = gtk.Image()
		image.set_from_file("./dna.jpeg")
		image_box.pack_start(image, True, False, 0)
		vertical_alignment.pack_start(image_box, False, False, 12)
		image_box.show()
		image.show()
		dna_seq_box = gtk.HBox(False, 0)
		#a label for sequence
		labelbox = gtk.HBox(False, 0)
		input_label = gtk.Label("Input the Nucleotide Sequence :")
		labelbox.pack_start(input_label, False, False, 0)
		vertical_alignment.pack_start(labelbox, False, False, 3)
		input_label.show()
		labelbox.show()
		dna_seq = gtk.Entry()
		dna_seq_box.pack_start(dna_seq, True, True, 4)
		vertical_alignment.pack_start(dna_seq_box, False, False, 0)
		dna_seq_box.show()
		dna_seq.show()
		dna_seq_box = gtk.HBox(False, 0)
		labels = []
		outputboxes = []
		for x in range(0, 13):
			outputboxes.append(gtk.HBox(False, 0))
			labels.append(gtk.Label())
			labels[x].show()
			outputboxes[x].pack_start(labels[x], False, False, 0)
			outputboxes[x].show()
			vertical_alignment.pack_start(outputboxes[x], False, False, 4)
		txt = "Properties of DNA : "
		labels[0].set_text(txt)
		vertical_alignment.pack_start(dna_seq_box, False, False, 10)
		dna_seq_box.show()
		lastbox = gtk.HBox(False, 0)
		process_button = gtk.Button("Process DNA")
		process_button.connect("clicked", self.sample_calcu, dna_seq, labels)
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
		vertical_alignment.pack_start(image_box, False, False, 12)
		image_box.show()
		image.show()
		#a label for input box
		labelbox = gtk.HBox(False, 0)
		input_label = gtk.Label("Select the genbank of the suspects :")
		labelbox.pack_start(input_label, False, False, 0)
		vertical_alignment.pack_start(labelbox, False, False, 3)
		input_label.show()
		labelbox.show()
		#a box for open
		openbox = gtk.HBox(False, 0)
		self.text = gtk.Entry()
		openbox.pack_start(self.text, True, True, 5)
		button = gtk.Button("Open..")
		button.connect("clicked", self.file_browser)
		self.text.set_text("--No File Selected--")
		openbox.pack_start(button, False, False, 0)
		vertical_alignment.pack_start(openbox, False, False, 8)
		self.text.show()
		button.show()
		#a label for sequence
		labelbox = gtk.HBox(False, 0)
		input_label = gtk.Label("Input the Nucleotide Sequence :")
		labelbox.pack_start(input_label, False, False, 0)
		vertical_alignment.pack_start(labelbox, False, False, 3)
		input_label.show()
		labelbox.show()
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
		process_button = gtk.Button("Find")
		process_button.connect("clicked", self.dna_process)
		quit_button = gtk.Button("Quit", gtk.STOCK_QUIT)
		quit_button.connect("clicked", gtk.main_quit)
		lastbox.pack_start(process_button, True, False, 0)
		lastbox.pack_start(quit_button, True, False, 0)
		vertical_alignment.pack_end(lastbox, False, False, 0)
		process_button.show()
		quit_button.show()
		#add vertical box to the window
		nbk.append_page(vertical_alignment, gtk.Label("Criminal Finder"))
		vertical2 = self.page2()
		nbk.append_page(vertical2, gtk.Label("DNA analysis"))
		self.main_window.add(nbk)
		nbk.set_current_page(0)
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
