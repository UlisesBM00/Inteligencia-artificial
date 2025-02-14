import random

class AgenteHibrido:
    def __init__(self, meta=100):
        self.posicion = 0
        self.meta = meta
        self.pasos = 0
    
    # Capa reactiva: percepción inmediata
    def percibir_entorno(self):
        if self.posicion >= self.meta:
            return "meta"
        return random.choice(["despejado", "obstáculo"])

    # Capa deliberativa: planificación de acciones
    def decidir_accion(self, entorno):
        if entorno == "meta":
            return "parar"
        elif entorno == "obstáculo":
            return "saltar"
        else:
            return "avanzar"
    
    # Capa de aprendizaje: contar pasos
    def aprender(self):
        self.pasos += 1

    # Capa de acción: ejecuta la decisión
    def actuar(self, accion):
        if accion == "avanzar":
            self.posicion += 10
            print(f"🏃 Avanzando... Posición: {self.posicion}")
        elif accion == "saltar":
            print("🤸 Saltando obstáculo...")
        elif accion == "parar":
            print(f"🎉 ¡Meta alcanzada en {self.pasos} pasos!")
    

    def correr(self):
        while True:
            entorno = self.percibir_entorno()
            accion = self.decidir_accion(entorno)
            self.aprender()
            self.actuar(accion)
            if accion == "parar":
                break

carrera = AgenteHibrido()
carrera.correr()
