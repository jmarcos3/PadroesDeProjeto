"""6)Implemente um sistema de leitura de arquivos de configuração:
a) Defina uma classe abstrata para leitores de configuração.
b) Implemente leitores concretos para formatos específicos (JSON, XML,
YAML).
c) Utilize o Factory Method para instanciar o leitor apropriado com base no tipo
de arquivo de configuração.
"""
from abc import ABC, abstractmethod

# Interface para documentos(Creator)
class ConfigFiles(ABC):
  @abstractmethod
  def read(self):
    pass

#Classe completa dos documentos(Concrete Product)
class JSON(ConfigFiles):
  def read(self):
    print("Lendo JSON...")
class XML(ConfigFiles):
  def read(self):
    print("Lendo XML...")
class YAML(ConfigFiles):
  def read(self):
    print("Lendo YAML...")
  
#Concrete Creator
class Loader():
  def load_json(self) -> JSON:
    return JSON()
  def load_xml(self) -> XML:
    return XML()
  def load_yaml(self) -> YAML:
    return YAML()

def main():
  loader = Loader()

  json = loader.load_json()
  xml = loader.load_xml()
  yaml = loader.load_yaml()

  json.read()
  xml.read()
  yaml.read()



main()