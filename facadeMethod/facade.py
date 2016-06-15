from Additional import Additional, RodaLigaLeve, SistemaSom, FreioAbs, DVD

class facadeAdditional:
	def __init__(self):
		self.rodaLigaLeve = RodaLigaLeve()
		self.sistemaSom = SistemaSom()
		self.freioAbs = FreioAbs()
		self.dvd = DVD()

	def addItems(self):
		self.rodaLigaLeve.RodaLigaLeve(4)
		self.sistemaSom.SistemaSom(2)
		self.freioAbs.FreioAbs(4)
		self.dvd.DVD(1)
