class Car:
    model="Altima"

class Car:
    def __init__(self,model):
        self.model=model
        
    def stop(self):
        return f"This is Nissan{self.model}"
    def start(self):
        return f"Nissan{self.model} is starting"
    def speed(self):
        return f"Nissan{self.model} covers 200km/hr in 1hr"
   
