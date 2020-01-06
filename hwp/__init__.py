import olefile

class HWP5():
	'''
	h = HWP5("hello.hwp")
	h.structure()
	'''
	def __init__(self, filename):
		self.fp = open(filename, "rb")
		return

	def metadata(self):
		return
