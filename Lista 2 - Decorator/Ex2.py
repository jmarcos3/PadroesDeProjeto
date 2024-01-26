# O texto deve ter um método render() que renderize o texto básico e um método addStyle() que adicione um estilo ao texto. Os estilos podem ser, por exemplo, negrito, itálico, sublinhado ou fonte.
from abc import ABC,abstractmethod

# Componente base - Texto
class Text(ABC):
  @abstractmethod
  def render(self):
    pass

# ConcreteComponent - Texto Simples
class SimpleText(Text):
  def render(self):
    return "Texto Base"

# Decorator
class TextDecorator(Text,ABC):
  def __init__(self, text: Text):
    self.text = text
  @abstractmethod
  def render(self):
    pass
  @abstractmethod
  def addStyle(self):
    pass

#ConcreteDecorator - Negrito, Italico, Sublinhado ou Fonte
class BoldDecorator(TextDecorator):
  def render(self):
    return f"{self.text.render()}, em negrito"
  def addStyle(self):
    return self.render()
  
class ItalicDecorator(TextDecorator):
  def render(self):
    return f"{self.text.render()}, em italico"
  def addStyle(self):
    return self.render()
  
class UnderlinedDecorator(TextDecorator):
  def render(self):
    return f"{self.text.render()}, sublinhado"
  def addStyle(self):
    return self.render()
    
class FontDecorator(TextDecorator):
  def render(self):
    return f"{self.text.render()}, com fonte x"
  def addStyle(self):
    return self.render()
    
def main():
  #Uso do padrão decorator
  basic_text = SimpleText()
  print("Texto Base:", basic_text.render())

  italic_text = ItalicDecorator(basic_text)
  print("Texto em Italico", italic_text.addStyle())

  bold_and_italic_text = BoldDecorator(italic_text)
  print("Texto em negrito e italico:", bold_and_italic_text.addStyle())


main()