import olefile, pprint, zlib
import hwp.structure.v5 as v5

class HWP5():
	'''
	h = HWP5("hello.hwp")
	h.structure()
	'''
	def __init__(self, filename):
		self.fp = olefile.OleFileIO("test.hwp")
		return
	
	def header(self):
		stream = self.fp.openstream('FileHeader').read()
		return parser.fileheader(stream)
	
	def docinfo(self):
		stream = self.fp.openstream('DocInfo').read()
		return parser.docinfo(stream)
