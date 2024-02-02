"""4) Crie um sistema de carregamento de documentos:
a) Defina uma classe abstrata para documentos.
b) Implemente métodos de carregamento em subclasses concretas (PDF,
Word, HTML).
c) Utilize o Factory Method para criar instâncias de documentos de acordo com
o tipo de arquivo.
"""

from abc import ABC, abstractmethod

# Interface para documentos(Creator)
class Documents(ABC):
  @abstractmethod
  def load(self):
    pass

#Classe completa dos documentos(Concrete Product)
class PDF(Documents):
  def load(self):
    print("Carregando PDF...")
class Word(Documents):
  def load(self):
    print("Carregando Word...")
class Html(Documents):
  def load(self):
    print("Carregando Html...")
  
#Concrete Creator
class Loader():
  def load_pdf(self) -> PDF:
    return PDF()
  def load_word(self) -> Word:
    return Word()
  def load_html(self) -> Html:
    return Html()

def main():
  loader = Loader()

  pdf = loader.load_pdf()
  word = loader.load_word()
  html = loader.load_html()

  pdf.load()
  word.load()
  html.load()

main()