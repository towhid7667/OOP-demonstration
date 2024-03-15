#Problem of not using polymorphism
class Circle:                                          #model creation
    def render_circle(self):
        return "Circle geometry"

class Rectangle:                                      #model creation
    def render_rectangle(self):
        return "Rectangel geometry"

shapes = [Circle(), Rectange()]                       #Data creation

for s in shapes:                                     #Reporting
    if type(s) is Circle:
        print(s.render_circle())
    elif type(s) is Rectangle:
        print(s.render_rectangle())




# a polymorphic render method has created, so there is no inheritance and no sharing instance, so no base class is needed
class Circle:
    def render(self):
        return "Circle geometry"

class Rectangle:
    def render(self):
        return "Rectangel geometry"

shapes = [Circle(), Rectange()]

for s in shapes:
    print(s.render())



#another example without polymorphism
class Header:
    def __init__(self, text):
        self.text = text

    def format_header(self):
        return f"{self.text}\n{'=' * len(self.text)}"

class Paragraph:
    def __init__(self, text):
        self.text = text

    def format_paragraph(self):
        return f"\n{self.text}"

# now added polymorphism to both

class Text:
    def __init__(self, text):
        self.text = text

class Header(Text):
    def format(self):
        return f"{self.text}\n{'=' * len(self.text)}"

class Paragraph(Text):
    def format(self):
        return f"\n{self.text}"

document = [
    Header("Polymorhism"),
    Paragraph("The secret weapon of software engineering is polymorphism."),
]

for d in document:
    print(d.format())

#another method added
class Text:
    def __init__(self, text):
        self.text = text

class Header(Text):
    def format(self):
        return f"{self.text}\n{'=' * len(self.text)}"

class Paragraph(Text):
    def format(self):
        return f"\n{self.text}"

class UppercaseParagraph(Text):
    def format(self):
        return f"\n{self.text.upper()}"

document = [
    Header("Polymorhism"),
    Paragraph("The secret weapon of software engineering is polymorphism."),
    UppercaseParagraph("Polymorphism prevents type switching."),
]

for d in document:
    print(d.format())    