from models import classes

class CitizenHandler:
    def __init__(self):
        self.citizens = classes.Queue()
    
    def add_citizen(self, citizen=None):
        if citizen:
            self.citizens.enqueue(citizen)
        else:           
            cedula = input("Ingrese cédula: ")
            nombre = input("Ingrese nombre completo: ")
            tramite = input("Ingrese tipo de trámite: ")
            hora = input("Ingrese hora de llegada: ")
            nuevo_ciudadano = classes.Citizen(cedula, nombre, tramite, hora)
            self.citizens.enqueue(nuevo_ciudadano)
    
    def show_next_citizen(self):
        return self.citizens.peek()
    
    def serve_citizen(self):
        self.citizens.dequeue()