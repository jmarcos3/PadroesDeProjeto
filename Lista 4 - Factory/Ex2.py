"""2) Desenvolva um sistema de widgets para uma GUI:
a) Crie uma hierarquia de classes para botões, caixas de texto e menus.
b) Defina uma fábrica abstrata para cada tipo de widget.
c) Implemente fábricas concretas para diferentes estilos de GUI (por exemplo,
estilo moderno, estilo clássico).
"""
from abc import ABC, abstractmethod

# Interface para os widgets
class Widget(ABC):
  @abstractmethod
  def createComponent(self):
    pass

#Abstract Facotry para Widgets(Creator)
class WidgetsFactory(ABC):
  @abstractmethod
  def produce_button(self):
    pass

  @abstractmethod
  def produce_InputText(self):
    pass

  def produce_Menus(self):
    pass
# Classe completa dos Widgets(Concrete Product)
class Button(Widget):
  def createComponent(self):
    print("Criando um botão")

class InputText(Widget):
  def createComponent(self):
    print ("Criando uma caixa de texto")

class Menus(Widget):
  def createComponent(self):
    print ("Criando um menu")

#Concrete Factory para Widgets (Concrete Creator)
class ClassicStyleFactory(WidgetsFactory):
  def produce_button(self):
    return Button()
  
  def produce_InputText(self):
    return InputText()
  
  def produce_Menus(self):
    return Menus()
  
class ModernStyleFactory(WidgetsFactory):
  def produce_button(self):
    return Button()
  
  def produce_InputText(self):
    return InputText()
  
  def produce_Menus(self):
    return Menus()
  
def main():
  classic_factory = ClassicStyleFactory()
  modern_factory = ModernStyleFactory()

  button1 = classic_factory.produce_button()
  inputtext1 = classic_factory.produce_InputText()
  menu1 = classic_factory.produce_Menus()

  button2 = modern_factory.produce_button()
  inputtext2 = modern_factory.produce_InputText()
  menu2 = modern_factory.produce_Menus()

  button1.createComponent()
  inputtext1.createComponent()
  menu1.createComponent()

  button2.createComponent()
  inputtext2.createComponent()
  menu2.createComponent()

main()