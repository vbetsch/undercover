class Menu:
    def __init__(self, title, *options):
        self.title = title
        self.options = options

    def show(self):
        result = f"--------------- {self.title.upper()} ---------------\n"
        for opt in self.options:
            result += f"({opt[0].lower()}) {opt[0]}\n"
        print(result)
