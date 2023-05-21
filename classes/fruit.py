class Fruit:
    texture="smooth"
    size="big"
    shape="circular"
    color="orange"

class Fruit:
    def __init__(self,texture,size,shape,color):
        self.texture=texture
    def grow(self):
        return f"Orange is {self.texture}"
    def ripe(self):
        return f"Orange is {self.texture} and radial"
    def rot(self):
        return f"Orange is {self.texture} and orange in color"
    
