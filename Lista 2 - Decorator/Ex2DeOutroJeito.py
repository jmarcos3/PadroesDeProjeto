# O texto deve ter um método render() que renderize o texto básico e um método addStyle() que adicione um estilo ao texto. Os estilos podem ser, por exemplo, negrito, itálico, sublinhado ou fonte.
from abc import ABC, abstractmethod

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
class TextDecorator(Text, ABC):
    def __init__(self, text: Text):
        self.text = text
        self.style = ""

    def render(self):
        return f"{self.text.render()}, {self.style}"

    def addStyle(self, style):
        self.style += style

#ConcreteDecorator - Negrito, Italico, Sublinhado ou Fonte
class BoldDecorator(TextDecorator):
    def __init__(self, text: Text):
        super().__init__(text)
        self.addStyle("em negrito")

class ItalicDecorator(TextDecorator):
    def __init__(self, text: Text):
        super().__init__(text)
        self.addStyle("em itálico")

class UnderlinedDecorator(TextDecorator):
    def __init__(self, text: Text):
        super().__init__(text)
        self.addStyle("sublinhado")

class FontDecorator(TextDecorator):
    def __init__(self, text: Text):
        super().__init__(text)
        self.addStyle("com fonte x")

def main():
     # Uso do padrão decorator
    basic_text = SimpleText()
    print("Texto Base:", basic_text.render())

    italic_text = ItalicDecorator(basic_text)
    print("Texto em Italico:", italic_text.render())

    bold_and_italic_text = BoldDecorator(italic_text)
    print("Texto em negrito e italico:", bold_and_italic_text.render())

main()
