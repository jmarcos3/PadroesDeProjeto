"""8)Desenvolva um sistema de geração de relatórios:
a) Implemente diferentes tipos de relatórios (PDF, CSV, HTML) como
subclasses.
b)Utilize o Factory Method para criar instâncias de relatórios conforme
necessário.

"""
from abc import ABC, abstractmethod

# Interface para documentos(Creator)
class Report(ABC):
  @abstractmethod
  def generate(self):
    pass

#Classe completa dos documentos(Concrete Product)
class PDF(Report):
  def generate(self):
    print("Gerando PDF...")
class CSV(Report):
  def generate(self):
    print("Gerando CSV ...")
class HTML(Report):
  def generate(self):
    print("Gerando HTML...")
  
#Concrete Creator
class Loader():
  def load_pdf(self) -> PDF:
    return PDF()
  def load_csv(self) -> CSV:
    return CSV()
  def load_html(self) -> HTML:
    return HTML()

def main():
  loader = Loader()

  pdf = loader.load_pdf()
  csv = loader.load_csv()
  html = loader.load_html()

  pdf.generate()
  csv.generate()
  html.generate()



main()