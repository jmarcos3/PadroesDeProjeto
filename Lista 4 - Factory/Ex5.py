"""5)Desenvolva um jogo com diferentes tipos de inimigos:
a) Crie uma classe abstrata para representar inimigos.
b) Implemente subclasses para diferentes tipos de inimigos (soldado, monstro,
chefe).
c) Use o Factory Method para criar instâncias de inimigos conforme o
progresso do jogo.
"""

from abc import ABC, abstractmethod
#Classe jogador
class Player():
  def __init__(self,nome,level):
    self.nome = nome
    self.level = level

# Interface para documentos(Creator)
class Enemies(ABC):
  @abstractmethod
  def sound(self):
    pass

#Classe completa dos documentos(Concrete Product)
class Orc(Enemies):
  def sound(self):
    print("Um orc")
class Troll(Enemies):
  def sound(self):
    print("Um troll")
class Undead(Enemies):
  def sound(self):
    print("Um undead" )
class Humanoid(Enemies):
  def sound(self):
    print("Um humano")
  
#Concrete Creator
class Create():
  def SetEnemy(self, Player: Player):
    match Player.level:
      case "1": return Orc()
      case "2": return Troll()
      case "3": return Undead()
      case "4": return Humanoid()


def main():
  player = Player("Marcos","2")
  pareador = Create()

  inimigo = pareador.SetEnemy(player)
  inimigo.sound()


main()