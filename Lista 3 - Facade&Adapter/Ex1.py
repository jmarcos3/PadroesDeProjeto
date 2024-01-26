""" 1) Considere uma classe Cliente que precisa interagir com uma classe BaseDeDados
para efetuar operações de cadastro, recuperação, atualização e remoção de
instâncias de uma classe Modelo que possui vários Elementos. O Cliente precisa
estabelecer uma conexão como a BaseDeDados receber uma instância de uma
classe Conexão e a partir da Conexão efetuar as operações desejadas. Forneça uma
solução utilizando padrões que simplifique a interação do Cliente com as demais
classes deste subsistema."""
"""Referencias: 
https://refactoring.guru/pt-br/design-patterns/facade/python/example#:~:text=O%20Facade%20%C3%A9%20um%20padr%C3%A3o,indesejadas%20para%20um%20s%C3%B3%20local.
https://refactoring.guru/pt-br/design-patterns/facade"""
#----------------------------------------------------------------
# Classe Base de Dados
class DataBase:
  def register(self):
    return print("Objeto registrado")
  def recover(self):
    return print("Objeto recuperado")
  def update(self):
    return print("Objeto atualizado")
  def remove(self):
    return print("Objeto removido")
# Classe Façade
class Facade:
  def __init__(self,subsystem1: DataBase):
    self.subsystem1 = subsystem1

  def operations(self):
    value = input("Qual operação deseja fazer? 1- Registrar, 2- Recuperar, 3- Atualizar, 4- Remover:    ")

    match value:
      case "1": self.subsystem1.register()
      case "2": self.subsystem1.recover()
      case "3": self.subsystem1.update()
      case "4": self.subsystem1.remove()
      case _: print("Opção invalida")

# Cliente que usará o sistema
def client_code(facade: Facade):
  facade.operations()
     
def main():
  # Inicializando o subsistema
  subsystem1 = DataBase()
  # Inicialziando o façade
  facade = Facade(subsystem1)
  # Cliente utilizando o sistema via façade
  client_code(facade)

main()