#3. ** Implemente um sistema de notícias que notifique aos interessados sempre que uma nova notícia for publicada.
class Noticias:
  
  def PublicarNoticia():
    Noticias.NotificarInteressados()

  def NotificarInteressados():
    for obj in Interessado.ListaDeInteressados:
      print("{} noticia quentinha saindo, vá conferir no portal " .format(obj.nome))

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
  Noticias.PublicarNoticia()
  Noticias.PublicarNoticia()
  Noticias.PublicarNoticia()


main()