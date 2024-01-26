#2. ** Implemente um sistema de alerta de temperatura que envie notificações para seus observadores sempre que a temperatura mudar.
class Controle:
  Temperatura = 20
  def AumentarTemperatura():
    Controle.Temperatura += 1 
    Controle.NotificarInteressados(Controle.Temperatura)

  def DiminuirTemperatura():
    Controle.Temperatura -= 1 
    Controle.NotificarInteressados(Controle.Temperatura)

  def NotificarInteressados(Temperatura):
    for obj in Interessado.ListaDeInteressados:
      print("{} A nova temperatura é: {}" .format(obj.nome,Temperatura))

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
  Controle.AumentarTemperatura()
  Controle.AumentarTemperatura()
  Controle.DiminuirTemperatura()


main()