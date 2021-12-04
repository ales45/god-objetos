class persona():
    dormir = "no"
    def __init__(self,ojos):
        self.ojos = input("como tienes los ojos:a ") 
    def dormir(self):
        if self.ojos == "abiertos":
            self.ojos = "cerrados"
            self.dormir = "si"
            return "ojos cerrados y a dormir"
        elif self.ojos == "cerrados":
            return "muy bien a dormir"
        else:
            return "FILO DA PUTA"
a = persona("abiertos")
print(a.dormir())