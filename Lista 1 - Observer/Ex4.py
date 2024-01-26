#4. ** Implemente um sistema de estoque que envie notificações para aqueles que monitoram sempre que a quantidade de um produto mudar.
class ControleEstoque:
  def __init__(self,nome,qtd):
    self.nome = nome
    self.qtd = qtd

  def EntradaProduto(self):
    self.qtd += 1 
    ControleEstoque.NotificarInteressados(self)

  def SaidaProduto(self):
    self.qtd -= 1 
    ControleEstoque.NotificarInteressados(self)

  def NotificarInteressados(self):
    for obj in Interessado.ListaDeInteressados:
      print("{} a nova quantidade do produto {} é: {}" .format(obj.nome,self.nome,self.qtd))

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
  Celular = ControleEstoque("Celular", 10)
  Televisao = ControleEstoque("Televisao",5)
  
  Celular.EntradaProduto()
  Televisao.SaidaProduto()

main()