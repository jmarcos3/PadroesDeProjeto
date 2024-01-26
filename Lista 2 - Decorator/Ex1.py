# O café deve ter um método prepare() que prepare o café básico e um método addIngredient() que adicione um ingrediente ao café. Os ingredientes podem ser, por exemplo, leite, açúcar, chocolate ou chantilly.
from abc import ABC,abstractmethod

#Componente base - Café
class Coffee(ABC):
  @abstractmethod
  def prepare(self):
    pass

#ConcreteComponent - Café Simples
class SimpleCoffee(Coffee):
  def prepare(self):
    return "Café Simples"
  
# Decorator - Ingredientes
class CoffeeDecorator(Coffee,ABC):
  def __init__(self,coffee: Coffee):
    self.coffe = coffee
  
  @abstractmethod
  def prepare(self):
    pass
  
#ConcreteDecorator - Leite
class MilkDecorator(CoffeeDecorator):
  def prepare(self):
    return (self.coffe.prepare()+ " com leite")

#ConcreteDecorator - Açucar
class SugarDecorator(CoffeeDecorator):
  def prepare(self):
    return (self.coffe.prepare()+ " com açúcar")

#ConcreteDecorator - Chocolate
class ChocolateDecorator(CoffeeDecorator):
  def prepare(self):
    return (self.coffe.prepare()+ " com chocolate")
    
#ConcreteDecorator - Chantily
class WhippedCreamDecorator(CoffeeDecorator):
  def prepare(self):
    return (self.coffe.prepare()+ " com chantily")

def main():
  #Usando o decorator
  basic_coffee = SimpleCoffee()
  coffee_with_milk_and_sugar = SugarDecorator(MilkDecorator(basic_coffee))
  coffee_with_chocolate_and_whipped_cream = WhippedCreamDecorator(ChocolateDecorator(basic_coffee))

  # Exemplo de preparo
  print("Café básico:", basic_coffee.prepare())
  print("Café com leite e açúcar:", coffee_with_milk_and_sugar.prepare())
  print("Café com chocolate e chantilly:", coffee_with_chocolate_and_whipped_cream.prepare())

main()