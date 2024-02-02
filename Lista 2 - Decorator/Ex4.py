#Adote o padrão decorator na classe Botao, incluindo o método render(). Este método deve tratar da renderização do botão básico, enquanto permitindo a definição de bordas simples, duplas ou tracejadas.
from abc import ABC,abstractmethod

#Componente base - Botão
class Button(ABC):
  @abstractmethod
  def render(self):
    pass

#ConcreteComponent - Botão Simples
class SimpleButton(Button):
  def render(self):
    return "Botão Simples"
  
# Decorator - Bordas
class ButtonDecorator(Button,ABC):
  def __init__(self,edges: Button):
    self.edges = edges
  
  @abstractmethod
  def render(self):
    pass
  
#ConcreteDecorator - Simples
class SimpleDecorator(ButtonDecorator):
  def render(self):
    return (self.edges.render()+ " bordas simples")

#ConcreteDecorator - duplas
class DoubleDecorator(ButtonDecorator):
  def render(self):
    return (self.edges.render()+ " bordas duplas")

#ConcreteDecorator - tracejadas
class DashedDecorator(ButtonDecorator):
  def render(self):
    return (self.edges.render()+ " bordas tracejadas")
  

def main():
  #Usando o decorator
  basic_button = SimpleButton()
  simple_edge_button = SimpleDecorator(basic_button)
  double_and_dashed_button = DoubleDecorator(DashedDecorator(basic_button))



  # Exemplo de preparo
  print("Botão Simples:", basic_button.render())
  print("Botão simples com bordas simples", simple_edge_button.render())
  print("Botão Simples com bordas tracejadas e bordas duplas:", double_and_dashed_button.render())

main()