"""7)Construa um sistema de registro de eventos:
a) Crie uma hierarquia de classes para representar diferentes tipos de eventos
(erro, aviso, informativo).
b) Implemente um Factory Method para criar instâncias de eventos com base
no tipo.

"""
from abc import ABC, abstractmethod

# Interface para documentos(Creator)
class Events(ABC):
  @abstractmethod
  def represent(self):
    pass

#Classe completa dos documentos(Concrete Product)
class Error(Events):
  def represent(self):
    print("Error...")
class Warning(Events):
  def represent(self):
    print("Aviso ...")
class Informative(Events):
  def represent(self):
    print("Informativo...")
  
#Concrete Creator
class Loader():
  def load_error(self) -> Error:
    return Error()
  def load_warning(self) -> Warning:
    return Warning()
  def load_informative(self) -> Informative:
    return Informative()

def main():
  loader = Loader()

  erro = loader.load_error()
  aviso = loader.load_warning()
  informativo = loader.load_informative()

  erro.represent()
  aviso.represent()
  informativo.represent()



main()