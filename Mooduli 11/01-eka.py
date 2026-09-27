class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(self.name)

class Book(Publication):
    def __init__(self, name, author, pages):
        self.author = author
        self.pages = pages
        super().__init__(name)
        

    def print_information(self):
        super().print_information()
        print(f"author {self.author}, {self.pages} pages")


class Magazine(Publication):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)
        

    def print_information(self):
        super().print_information()
        print(f"Chief editor {self.editor}")



m1 = Magazine("Donald Duck", "Aki Hyyppä")
b1 = Book("Compartment No. 6", "Rosa Liksom", 192)

m1.print_information()
b1.print_information()