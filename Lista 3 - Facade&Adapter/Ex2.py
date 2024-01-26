""" 2) Uma classe Cliente precisa requisitar serviços de uma classe preexistente cuja
interface não é a interface esperada pela classe Cliente. Estabeleça uma solução
usando padrões que resolva o problema de discrepância das interface"""
"""Referências:
https://refactoring.guru/pt-br/design-patterns/adapter/python/example
https://refactoring.guru/pt-br/design-patterns/adapter"""

#--------------------------------------------------------------
class Target:
  def request(self):
    return "Alvo que meu cliente deseja(interface)"
#Classe a ser adaptada
class Adaptee:
  def specific_request(self):
    return "ajesed etneilc uem euq ecafretnI"
#Classe adaptando
class Adapter(Target, Adaptee):
  def request(self):
    return f"Interface Traduzida: {self.specific_request()[::-1]}" 
  
def client_code(target: Target):
  print(target.request())

def main():
  target = Target()
  client_code(target)
  
  print("\n")
  adaptee = Adaptee()
  print("Interface que meu cliente precisa porem ele não entende, precisa de um adaptador:")
  print(adaptee.specific_request())

  print("\n")
  print("Com adaptador:")
  adapter = Adapter()
  client_code(adapter)

main()