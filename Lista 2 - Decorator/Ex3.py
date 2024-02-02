# Aplique o padrão decorator à classe FiguraGeometrica, introduzindo o método render(). Este método deve abordar a renderização da figura geométrica básica, enquanto proporciona a capacidade de definir cores como preto, branco, vermelho, verde ou azul.
from abc import ABC,abstractmethod

#Componente base - Figura Geometrica
class GeometricFigure(ABC):
  @abstractmethod
  def render(self):
    pass

#ConcreteComponent - Figura Simples
class SimpleFigure(GeometricFigure):
  def render(self):
    return "Figura Simples"
  
# Decorator - Cores
class FigureDecorator(GeometricFigure,ABC):
  def __init__(self,figure: GeometricFigure):
    self.figure = figure
  
  @abstractmethod
  def render(self):
    pass
  
#ConcreteDecorator - Preto
class BlackDecorator(FigureDecorator):
  def render(self):
    return (self.figure.render()+ " preto")

#ConcreteDecorator - Branco
class WhiteDecorator(FigureDecorator):
  def render(self):
    return (self.figure.render()+ " branco")

#ConcreteDecorator - Vermelho
class RedDecorator(FigureDecorator):
  def render(self):
    return (self.figure.render()+ " vermelho")
    
#ConcreteDecorator - Verde
class GreenDecorator(FigureDecorator):
  def render(self):
    return (self.figure.render()+ " verde")
  
#ConcreteDecorator - Azul
class BlueDecorator(FigureDecorator):
  def render(self):
    return (self.figure.render()+ " azul")
  


def main():
  #Usando o decorator
  basic_figure = SimpleFigure()
  red_and_white_figure = WhiteDecorator(RedDecorator(basic_figure))
  black_and_blue_figure = BlueDecorator(BlackDecorator(basic_figure))


  # Exemplo de preparo
  print("Figura simples:", basic_figure.render())
  print("Figura simples vermelho branco:", red_and_white_figure.render())
  print("Figura simples preto azul:", black_and_blue_figure.render())

main()