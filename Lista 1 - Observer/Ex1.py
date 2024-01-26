#1. ** Implemente um contador de cliques que notifique a quem estiver interessado sempre que o número de cliques mudar.
class Cliques:
  QtdCliques = 0
  def RealizarClique():
    Cliques.QtdCliques += 1 
    Cliques.NotificarInteressados(Cliques.QtdCliques)

  def NotificarInteressados(QtdCliques):
    for obj in Interessado.ListaDeInteressados:
      print("{} A quantidade de cliques aumentou para {}" .format(obj.nome,QtdCliques))

class Interessado:
  ListaDeInteressados = []

  def __init__(self,nome,interesse):
    self.nome = nome
    self.interesse = interesse
    if self.interesse == 1:
      Interessado.ListaDeInteressados.append(self)
    else:
      pass


def main():
  Interessado1 = Interessado("João",1)
  Interessado2 = Interessado("Maria",1)
  NaoInteressado = Interessado("Marcos",0)
  Cliques.RealizarClique()
  Cliques.RealizarClique()
  Cliques.RealizarClique()


main()