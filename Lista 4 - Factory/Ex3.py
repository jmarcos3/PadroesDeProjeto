"""3) Simulação de construção de casas:
a) Defina uma hierarquia de classes para diferentes partes de uma casa
(fundação, paredes, telhado).
b) Crie uma fábrica abstrata para cada parte da casa.
c) Implemente fábricas concretas para diferentes estilos arquitetônicos (por
exemplo, estilo contemporâneo, estilo colonial).
"""
from abc import ABC, abstractmethod

# Interface para os elementos da casa
class HouseComponent(ABC):
  @abstractmethod
  def createComponent(self):
    pass

# Abstract facotry para os elementos da casa
class HouseComponentsFactory(ABC):
  @abstractmethod
  def produce_foundation(self):
    pass
  @abstractmethod
  def produce_wall(self):
    pass
  @abstractmethod
  def produce_roof(self):
    pass
  @abstractmethod
  def produce_door(self):
    pass

# Classe Completa dos elementos da casa(Concrete Product) 
class Foundation(HouseComponent):
  def createComponent(self):
    print ("Criando fundação")

class Wall(HouseComponent):
  def createComponent(self):
    print ("Criando paredes")

class Roof(HouseComponent):
  def createComponent(self):
    print ("Criando telhados")

class Door(HouseComponent):
  def createComponent(self):
    print ("Criando porta")

#Concrete Factory p/ HouseComponents  
class Estilo1Factory(HouseComponentsFactory):
  def produce_foundation(self):
    return Foundation()
  def produce_wall(self):
    return Wall()
  def produce_roof(self):
    return Roof()
  def produce_door(self):
    return Door()

class Estilo2Factory(HouseComponentsFactory):
  def produce_foundation(self):
    return Foundation()
  def produce_wall(self):
    return Wall()
  def produce_roof(self):
    return Roof()
  def produce_door(self):
    return Door()

def main():
  estilo1_factory = Estilo1Factory()
  estilo2_factory = Estilo2Factory()

  foundation1 = estilo1_factory.produce_foundation()
  wall2 = estilo2_factory.produce_wall()
  roof1 = estilo1_factory.produce_roof()
  door2 = estilo2_factory.produce_door()

  foundation1.createComponent()
  wall2.createComponent()
  roof1.createComponent()
  door2.createComponent()

main()