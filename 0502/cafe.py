class Cafe:
    cafename = ""
    menu = ""
    cupSize = ""
    
    def __init__(self, name, menu):
        self.cafeName = name
        self.menu = menu

    def ordering(self,cupSize):
        self.cupSize = cupSize
        print(f"Order: {self.menu}, Size: {self.cupSize}")