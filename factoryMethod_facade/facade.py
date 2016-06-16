from addtional import RodaLigaLeve, SistemaSom, FreioAbs, DVD

class facadeAdditional:
	def __init__(self):
		self.roda= RodaLigaLeve()
		self.som = SistemaSom()
		self.freio = FreioAbs()
		self.midia = DVD()

	def addItems(self):

		self.roda.rodaLigaLeve()
	
		self.som.sistemaSom()
	
		self.freio.freioAbs()
	
		self.midia.dvd()

